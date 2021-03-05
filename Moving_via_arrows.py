# Import the necessary libraries
#import time
#import math
#from ev3dev2.motor import *
import keyboard
import pynput.keyboard as pynput
import msvcrt as m



def wait():
    m.getch()


#motorA = LargeMotor(OUTPUT_A)
#motorB = LargeMotor(OUTPUT_B)


#There will be motions soon
while True:
    if keyboard.is_pressed('up arrow'):
        wait()
        print('go strait')
        #motorA.on(20)
        #motorA.off(brake=True)
    elif keyboard.is_pressed('left arrow'):
        wait()
        print('go left')
        #motorB.on(20)
        #motorB.off(brake=True)
    elif keyboard.is_pressed('down arrow'):
        wait()
        print('go back')
        #motorA.on(-20)
        #motorA.off(brake=True)    
    elif keyboard.is_pressed('right arrow'):
        wait()
        print('go right')
        #motorB.on(-20)
        #motorB.off(brake=True)    
    elif keyboard.is_pressed('ctrl+c'):
        print('It is the END of our WORK')
        break
    wait()