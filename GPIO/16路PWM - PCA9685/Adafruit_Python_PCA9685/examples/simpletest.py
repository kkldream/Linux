from __future__ import division
import time
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()
servo_min = 150  # 0~4096
servo_max = 665
pwm.set_pwm_freq(60)
def servoWrite(channel, pulse):
    if pulse >= 0 and pulse <= 100:
        pulse = int(pulse / 100 * (servo_max - servo_min) + servo_min)
        pwm.set_pwm(channel, 0, pulse)
        print(pulse)
        return 0
    return -1
while True:
    pulse = int(input('pulse='))
    pwm.set_pwm(0, 0, pulse)
    #servoWrite(0, var)
