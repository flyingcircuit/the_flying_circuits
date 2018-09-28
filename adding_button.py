from gpiozero import LED, Button
from time import sleep

red = LED(20)
switch = Button(21)
while True:
    if switch.is_pressed: 
        print('Switch has been pressed')
        
    else:
        print('Press the switch!')
