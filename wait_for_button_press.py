from gpiozero import LED, Button
from time import sleep

red = LED(20)
switch = Button(21)

def flasher():
    while True:
        red.on()
        sleep(1)
        red.off()
        sleep(1)

switch.when_pressed() = flasher


