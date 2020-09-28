import io
import picamera
import logging
import socketserver
from threading import Condition
import threading
from http import server
import time
temperature = -1
humidity = -1
soil_moisture = -1
end = False

import Adafruit_DHT
DHT11_GPIO_PIN = 4
def dht22():
    print('DHT22 Start')
    while end == False:
        global humidity, temperature
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, DHT11_GPIO_PIN)
        humidity = int(humidity * 10) / 10
        temperature = int(temperature)
        print('溫度=%.1f度C 濕度=%d百分比' %(temperature, humidity))
        time.sleep(5)
thread_dht22 = threading.Thread(target = dht22)


import Adafruit_GPIO.SPI, Adafruit_MCP3008
adc = Adafruit_MCP3008.MCP3008(spi=Adafruit_GPIO.SPI.SpiDev(0, 0))
SOIL_ADC_PIN = 0
def soil():
    MAX = 650
    print('soil_moisture Start')
    while end == False:
        global soil_moisture
        soil_moisture = adc.read_adc(SOIL_ADC_PIN)
        if soil_moisture > MAX: soil_moisture = 100
        else: soil_moisture = int(soil_moisture / MAX * 100)
        print('土壤濕度=%d百分比' %soil_moisture)
        time.sleep(1)
thread_soil = threading.Thread(target = soil)

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index':
            str1 = '溫度 = ' + str(temperature) + "度"
            str2 = '濕度 = ' + str(humidity) + "%"
            str3 = '土壤濕度 = ' + str(soil_moisture) + "%"
            PAGE = \
            '''
            <html>
                <head>
                    <meta charset='utf-8'/>
                    <title>智慧農場</title>
                    <style>body { font-family: '微軟正黑體', '黑體-繁', Sans-Serif;}</style>
                </head>
                <body>
                    <center><h1>智慧農場</h1></center>
                    <center><img src="stream.mjpg" width="640" height="480"></center>
                    <center><h2>''' + str1 + '''</h2></center>
                    <center><h2>''' + str2 + '''</h2></center>
                    <center><h2>''' + str3 + '''</h2></center>
                </body>
            </html>
            '''
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/data':
            PAGE = str(temperature) + "," + str(humidity) + "," + str(soil_moisture)
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

thread_dht22.start()
thread_soil.start()
with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    #Uncomment the next line to change your Pi's Camera rotation (in degrees)
    camera.rotation = 180
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        end = True
        camera.stop_recording()
        print('Camera Finally')