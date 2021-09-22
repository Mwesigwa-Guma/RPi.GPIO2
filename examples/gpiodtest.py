import gpiod

try:
    chip = gpiod.Chip("/sys/class/pwm/pwmchip0/pwm0/enable")
except PermissionError:
    print("you don't have permission to access /../.../../..")
    sys.exit()
