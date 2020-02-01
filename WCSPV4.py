#!/usr/bin/env micropython
#Change the language to "micropython" for more speed, and "python3" for more functionality

#Import functions
from ev3dev2.motor import * #Motors, for moving
from time import sleep #Timers, for waiting
from ev3dev2.sensor.lego import ColorSensor #Sensors, for sensing
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2 #Ports, for sensors to be plugged into
from ev3dev2.button import * #Buttons, for Master program control
from ev3dev2.led import *
#Import our files
import WCSUtilities as Util
from StuffInCircle import * 
from Crane import *
from Alift import *
from Cake import *
from TheStick import *
from Bridge import *
from GoForIt import *
from Architecture import *
from BigLong import *
from DesignBuild import *
from NewBridge import *

#Define motors and sensors
Arm = LargeMotor(OUTPUT_A) #Up and down motion
DriveBase = MoveSteering(OUTPUT_B,OUTPUT_C, motor_class=MediumMotor) #Driving
Pusher = MediumMotor(OUTPUT_D) #Out and in and rotating motions
CSL = ColorSensor(INPUT_1) #Color sensors
CSR = ColorSensor(INPUT_2) #Color sensors
USS = UltrasonicSensor() #Ultrasonic sensor
Lights = Leds()
#Defines buttons
Btn = Button()
#Defines sensing motors
CMotSens = MediumMotor(OUTPUT_C)
BMotSens = MediumMotor(OUTPUT_B)
Lights.all_off()
while True:
    while True: #Makes it so we can have more programs and not have to press the back button.
        DriveBase.off(brake=False)
        Arm.off(brake=False)
        Pusher.off(brake=False)
        Lights.set_color("LEFT","YELLOW")
        Lights.set_color("RIGHT","YELLOW")
        
        if(Btn.left):
            DesignBuild(DriveBase,Lights,Arm,Pusher,CSR) 
        if(Btn.up):
            BigLong(DriveBase,Arm,Pusher,CSL,CSR,USS,Btn,CMotSens,BMotSens,"up")
        if(Btn.right): 
            Architect(Arm, DriveBase, Pusher, CSL, CSR, USS, Lights, BMotSens, CMotSens)
        if(Btn.down):
            NewBridge (Arm,DriveBase,Pusher,CSL,CSR,USS,Btn,CMotSens,BMotSens,Lights)
        if(Btn.enter):
            Btn.wait_for_released("enter")
            print("New menu!")
            break
    while True:
        DriveBase.off(brake=False)
        Arm.off(brake=False)
        Pusher.off(brake=False)
        Lights.set_color("LEFT","RED")
        Lights.set_color("RIGHT","RED")
        if(Btn.left):
           StuffInCircle(DriveBase,Lights,Arm,Pusher,CSR)  
        if(Btn.up):
           Crane(DriveBase,Arm,CSL,CSR,BMotSens,CMotSens)
        if(Btn.right): 
            pass
        if(Btn.down):
            pass
        if(Btn.enter):
            Btn.wait_for_released("enter")
            break
