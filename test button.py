from gpiozero import DistanceSensor, LED, Button
from time import sleep

stop = LED(26)
start = LED(19)

reset = Button(17)

while True:
    if reset.is_pressed:
        print('pressed')

