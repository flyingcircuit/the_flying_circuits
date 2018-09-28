import math, random
from blinkt import set_pixel, show, clear
from time import sleep

def greeting():
    print('Hello, what would you like to do: a, b, or c?' )
    print('a for weather')
    print('b for mathmatical fun times')
    print('c for (limited) disco')
    choice = input()
    if choice == 'a':
        weather()
    elif choice == 'b':
        pythag()
    elif choice == 'c':
        disco()
    elif choice == 'VIVE LA FRANCE':
        tricolor()
    elif choice == 'quit':
        quit()
    else:
        print ('Invalid choice, please try again...')
        greeting()

def weather():
    name = input("What is your name? ")
    temp = int(input("What is the temp? "))

    if temp >= 50:
        print ("It's a scorcher! (the end is nigh)")
    elif 15 <= temp <50:
        print ("Hello " + name + ", it's looking good out there!")
    elif 7 <= temp < 15:
        print ("Hello " + name + ", could be chilly!")
    else:
        print ("Hello " + name + ", you might want a jacket!")
    print('')    
    greeting()

def pythag():
    a = int(input('Enter a number: '))
    b = int(input('Enter another number: '))
    print (math.hypot(a, b))
    print('')  
    greeting()
        
def disco():
    for i in range(1, 100):
        rand_led = random.randint(0,7)
        rand_col1 = random.randint(0,50)
        rand_col2 = random.randint(0,50)
        rand_col3 = random.randint(0,50)
        
        set_pixel(rand_led, rand_col1, rand_col2, rand_col3)
        
        sleep(0.0001)
        show()
    clear()
    show()
    print('')  
    greeting()

def tricolor():
    set_pixel(0, 200, 0, 0)
    set_pixel(1, 200, 0, 0)
    set_pixel(2, 200, 0, 0)
    set_pixel(3, 100, 100, 100)
    set_pixel(4, 100, 100, 100)
    set_pixel(5, 0, 0, 200)
    set_pixel(6, 0, 0, 200)
    set_pixel(7, 0, 0, 200)

    show()
    sleep(5)
    clear()
    show()
    print('')  
    greeting()
    
    

greeting()