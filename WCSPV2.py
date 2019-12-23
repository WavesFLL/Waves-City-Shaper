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


while True: #Master program which runs different programs depending on which button is pushed
    DriveBase.off(brake=False)
    Arm.off(brake=False)
    Pusher.off(brake=False)
    Lights.all_off()
    if(Btn.left):
       StuffInCircle(DriveBase,Lights,Arm,Pusher,CSR)  
    if(Btn.up):
       Crane(DriveBase,Arm,CSL,CSR,BMotSens,CMotSens)
    if(Btn.right): 
       Alift(DriveBase,Arm,Pusher,CSR,USS)
    if(Btn.down):
       Cake(DriveBase)
    if(Btn.enter):
       TheStick(DriveBase,Arm,Pusher,CSL,CSR,USS,Btn,CMotSens)
        #Need to add bridge