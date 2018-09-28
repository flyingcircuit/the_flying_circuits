from gpiozero import LED, Button
from time import sleep
import random

red = LED(16)
switch_yel = Button(21)
switch_red = Button(20)
randy_time = random.randint(0,5)

while True:
    def red_win():
        print('Red wins!')

    def yell_win():
        print('Yellow wins!')

    sleep(randy_time)
    red.on()

    switch_yel.when_pressed = yell_win
    switch_red.when_pressed = red_win
    

