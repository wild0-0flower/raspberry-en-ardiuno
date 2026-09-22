from gpiozero import Button
from gpiozero import LED
from signal import pause

button = Button(2)
red = LED(5)

button.when_pressed = red.toggle

pause()