import smbus
import time

bus = smbus.SMBus(1)
address = 0x04

def writeByte(value):
    bus.write_byte(address, value)

def readStatus():
    number = bus.read_byte(address)
    return number

if __name__ == '__main__':
    print('Arduino Status：%d' %readStatus())
    while True:
        value = int(input('Send：'))    #0~255
        writeByte(value)