#!/bin/python3
# PWM demo from Ben Croston
# source: https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/

# It works out of the box with no changes!

import time
import core
core.setmode(core.BOARD)

p = core.HardwarePWM(12, 50)  # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
core.cleanup()
