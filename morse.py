from gpiozero import LED, Button
from time import sleep

red = LED(26)
green = LED(19)
def do():
    red.on()
    sleep(0.2)
    red.off()
    sleep(0.4)
    
def da():
    red.on()
    sleep(1.2)
    red.off()
    sleep(0.4)

def space():
    green.on()
    red.on()
    sleep(2)
    red.off()
    green.off()

def sep():
    green.on()
    sleep(1.2)
    green.off()
    


dict = {'A' : [do,da,sep],
        'B' : [da,do,do,do,sep],
        'C' : [da,do,da,do,sep],
        'D' : [da,do,do,sep],
        'E' : [do,sep],
        'F' : [do,do,da,do,sep],
        'G' : [da,da,do,sep],
        'H' : [do,do,do,do,sep],
        'I' : [do,do,sep],
        'J' : [do,da,da,da,sep],
        'K' : [da,do,da,sep],
        'L' : [do,da,do,do,sep],
        'M' : [da,da,sep],
        'N' : [da,do,sep],
        'O' : [da,da,da,sep],
        'P' : [do,da,da,do,sep],
        'Q' : [da,da,do,da,sep],
        'R' : [do,da,do,sep],
        'S' : [do,do,do,sep],
        'T' : [da,sep],
        'U' : [do,do,da,sep],
        'V' : [do,do,do,da,sep],
        'W' : [do,da,da,sep],
        'X' : [da,do,do,da,sep],
        'Y' : [da,do,da,da,sep],
        'Z' : [da,da,do,do,sep],
        ' ' : [space]}    
your_msg = input('Please enter your message: ' )

for i in your_msg:
    for output_morse in dict[i.upper()]:
        output_morse()
