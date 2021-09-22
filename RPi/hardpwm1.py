#!/bin/python3
#from rpi_hardware_pwm import HardwarePWM
#import RPi.GPIO as GPIO
import core
import time
import pdb

core.setmode(core.BOARD)


pwm = core.HardwarePWM(35, 60)
pwm.start(50)
pwm.ChangeDutycycle(50)
time.sleep(3)
pwm.ChangeFrequency(25_000)
pwm.stop()
