from blinkt import set_pixel, show, clear
import random
from time import sleep

#while True:
for i in range(1, 1000):
    rand_led = random.randint(0,7)
    rand_col1 = random.randint(0,50)
    rand_col2 = random.randint(0,50)
    rand_col3 = random.randint(0,50)
    
    set_pixel(rand_led, rand_col1, rand_col2, rand_col3)
    
    sleep(0.0001)
    show()
     
    


