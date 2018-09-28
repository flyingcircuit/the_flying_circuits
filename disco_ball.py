from gpiozero import LED, Button
from time import sleep
import random

disco_red = LED(5)
disco_blue = LED(13)
disco_green = LED(6)
disco_button = Button(20)

def disco_ball():
    disco_red.on()
    sleep (1)      
    disco_red.off()
    disco_green.on()
    sleep (1)
    disco_green.off()
    disco_blue.on()
    sleep (1)
    disco_blue.off()
    
disco_button.when_pressed = disco_ball
