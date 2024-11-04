from gpiozero import LED
from signal import pause
light = LED(17)
light.blink()
pause()