# Import the necessary libraries
#import time
#import math
#from ev3dev2.motor import *
#from ev3dev2.sensor import INPUT_2
#from ev3dev2.sensor.lego import TouchSensor
import keyboard
import pynput.keyboard as pynput
import msvcrt as m



def wait():
    m.getch()


#motorA = LargeMotor(OUTPUT_A)
#motorB = LargeMotor(OUTPUT_B)
#ts = TouchSensor(INPUT_2)
#motorC = LargeMotor(OUTPUT_c)




#Checking if writer/eraser was pushed/pulled before
check_w=True
check_e=True

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
    elif keyboard.is_pressed('space'):
        check_w=not(check_w)
        if check_w:
            print('TAKE OFF the WRITERRRR')
            #motorC.on(-100)
            #motorC.off(brake=True)
        else: 
            print('Land the WRITERRRR')
                #while True:
                    #if ts1.value() == 0:
                        #motorC.stop(stop_action="brake")
                    #else:
                        #motorC.on(20)
    elif keyboard.is_pressed('backspace'):
        check_e=not(check_e)
        if check_e:
            print('TAKE OFF the ERASERRRR')
            #motorC.on(100)
            #motorC.off(brake=True)
        else: 
            print('Land the ERASERRR')
                #while True:
                    #if ts1.value() == 0:
                        #motorC.stop(stop_action="brake")
                    #else:
                        #motorC.on(-20)
    elif keyboard.is_pressed('ctrl+c'):
        print('It is the END of our WORK')
        break
    wait()
