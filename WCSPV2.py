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
CMOTSENS = MediumMotor(OUTPUT_C)
BMOTSENS = MediumMotor(OUTPUT_B)

#Moving smooth
def Smooth_C(steerings,speedie,revolutions):
    MotSensVar = CMOTSENS.position
    DriveBase.on(steering=steerings, speed=speedie)
    while(CMOTSENS.position<= (360*revolutions)+MotSensVar):
        pass
def Smooth_B(steerings,speedie,revolutions): 
    MotSensVar = BMOTSENS.position
    DriveBase.on(steering=steerings, speed=speedie)
    while(BMOTSENS.position<= (360*revolutions)+MotSensVar):
        pass
def RotInches(steerin,speedie,millimeters):
    DriveBase.on_for_rotations(steering=steerin,speed=speedie,rotations=millimeters/176)
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

while True: #Master program which runs different programs depending on which button is pushed
    DriveBase.off(brake=False)
    Arm.off(brake=False)
    Pusher.off(brake=False)
    Lights.all_off()
    if(Btn.left):
       StuffInCircle()
    if(Btn.up):
        Crane()
    if(Btn.right): 
        Alift()
    if(Btn.down):
        Cake()
    if(Btn.enter):
        TheStick()