#!/bin/python3
from rpi_hardware_pwm import HardwarePWM
#import RPi.GPIO as GPIO

pwm = HardwarePWM(pwm_channel=0, hz=60)
pwm.start(100)

pwm.change_duty_cycle(50)
pwm.change_frequency(25_000)

pwm.stop()
