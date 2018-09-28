from gpiozero import LED, Button
from time import sleep
import random

red = LED(26)
yellow = LED (19)
green = LED(22)
party_button = Button(17)
disco_on = False


def disco_red():
   red.blink(0.10)
   sleep (0.1)
   red.blink(0.6)
    
def disco_yellow():
    yellow.blink(0.10)
    sleep(0.1)
    yellow.blink(0.2)
    
    
def disco_green():
    green.blink(0.10)
    sleep(0.1)
    green.blink(0.4)

def disco_on():
    disco_red()
    disco_green()
    disco_yellow()
    
def disco_off():

    
def disco():
    global disco_on
    if disco_on:
        green.off()
        red.off()
        yellow.off()
        disco_on = False
    else:
        disco_red()
        disco_green()
        disco_yellow()
        disco_on = True 
    
party_button.wait_for_press = disco
            
