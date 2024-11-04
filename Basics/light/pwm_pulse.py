from gpiozero import PWMLED
from signal import pause

light = PWMLED(17)

light.pulse()

pause()