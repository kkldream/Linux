import time
import Adafruit_GPIO.SPI, Adafruit_MCP3008
try:
    print('start')
    while True:
        adc = Adafruit_MCP3008.MCP3008(spi=Adafruit_GPIO.SPI.SpiDev(0, 0))
        for a in range(8):
            var = adc.read_adc(a)
            print(var, end=', ')
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    print('KeyboardInterrupt')
finally:
    print('finally')