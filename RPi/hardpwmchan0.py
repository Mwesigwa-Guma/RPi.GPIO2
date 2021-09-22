import core
import time

core.setmode(core.BCM)
pwm = core.HardwarePWM(18, 50)
pwm.start(50)

time.sleep(3)

for i in range(10):
    pwm.ChangeFrequency(2 ** i)
    print("set frequency to", 2 ** i)
    time.sleep(3)

pwm.stop()
