from machine import Pin, PWM
import time

class PicoServo:
    def __init__(self, pin_num):
        self.servo_pin = Pin(pin_num)
        self.servo_pwm = PWM(self.servo_pin)
        self.servo_pwm.freq(50)  

    def set_angle(self, angle):
        duty_cycle = int(((angle / 180.0) * 2000) + 500)
        self.servo_pwm.duty_u16(duty_cycle * 65536 // 2500)