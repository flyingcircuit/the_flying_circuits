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
