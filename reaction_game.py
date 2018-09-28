from gpiozero import LED, Button
from time import sleep
import random

red = LED(16)
switch_yel = Button(21)
switch_red = Button(20)

randy_time = random.randint(0,5)
sleep(randy_time)
red.on()

def race():
    while True:
        sleep(0.1)
        if switch_yel.is_pressed:
            print('yellow won')
        elif switch_red.is_pressed:
            print('red won')
        
if red.on == True:
    race()


sleep(5)
red.off()



