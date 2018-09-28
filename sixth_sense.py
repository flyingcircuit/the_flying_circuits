from gpiozero import DistanceSensor, LED, Button
from time import sleep

you_cant_handle = True

    
stop = LED(26)
start = LED(19)
reset = Button(17)
sensor = DistanceSensor(echo=16, trigger=21)


def sixth_sense():
    you_cant_handle = True
    while you_cant_handle:
        if sensor.distance > 0:
            print('Distance:', sensor.distance * 100)
            start.on()
            sleep(0.1)
        
        if sensor.distance < 0.1:
            print('Stopstopstoparghhh')
            start.off()
            stop.on()
            you_cant_handle = False
            sleep(5)
            stop.off()
            if reset.wait_for_press():
                stop.off()
                sixth_sense()

sixth_sense()
            
            
