import os
import os.path

def cat(filename: str):
    with open(filename, "r") as file:
        return file.read()

print(cat("/sys/class/pwm/pwmchip0/pwm0/enable"))
