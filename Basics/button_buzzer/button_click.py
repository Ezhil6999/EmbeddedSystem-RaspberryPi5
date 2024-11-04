from gpiozero import Button
from time import sleep
from signal import pause

button = Button(17)

def say_hello():
    print("Hi Ezhil! you are going on the good way")
    sleep(2)
count =0 
while True:
    if button.wait_for_active():
        count = count +1
        print(count)

