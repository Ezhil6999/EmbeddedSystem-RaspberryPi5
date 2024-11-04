from gpiozero import PWMLED
from time import sleep

light = PWMLED(17)
while True:
    light.value = 0.5
    sleep(1)
    light.value = 1
    sleep(1)
    light.value = 0
    sleep(1)