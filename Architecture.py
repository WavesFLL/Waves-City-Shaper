#!/usr/bin/env micropython
#Import functions
from ev3dev2.motor import * #Motors, for moving
from time import sleep #Timers, for waiting
from ev3dev2.sensor.lego import ColorSensor #Sensors, for sensing
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2 #Ports, for sensors to be plugged into
from ev3dev2.button import * #Buttons, for Master program control
from ev3dev2.led import *
from time import sleep
import WCSUtilities as WCSUtil

def Architect(Arm, DriveBase, Pusher, CSL, CSR, USS, Lights, BMotSens, CMotSens):
    
    #Lifts up arm and waits for us to move our hands
    Arm.on_for_degrees(speed=15,degrees=-10)
    sleep(1)
    
    #Drives toward black line
    WCSUtil.Smooth(DriveBase, BMotSens, steerings=23,speedie=30,revolutions=1.25) 

    #Follows said line with the right color sensor, 
    #until left color sensor sees the edge of launch area
    while(CSL.reflected_light_intensity >= 30): 
        error = (45 - CSR.reflected_light_intensity)*0.9
        DriveBase.on(error, speed=22)
    DriveBase.off()  
    
    #Puts Architecture and design and build in the black circle Southeast of crane
    DriveBase.on_for_rotations(steering=40,speed=15,rotations=0.25)
    DriveBase.on_for_rotations(steering=0,speed=15,rotations=0.15)
    Pusher.on_for_degrees(speed=-10,degrees=100)
    DriveBase.on_for_rotations(steering=60,speed=15,rotations=0.5)
    
    #Follows wall to get the other design and build blocks into the red circle
    MotSensVar = CMotSens.position
    while(CMotSens.position<= (360*1)+MotSensVar): 
        error = (44.5 - USS.distance_centimeters)*8#used to be 10.5
        error = WCSUtil.constrain(error,-100,100)
        error = 0 - error
        DriveBase.on(steering=error,speed=35)
    DriveBase.on_for_rotations(steering=0,speed=35,rotations=0.8)
    
    #Lifts arm and drives back to base
    Arm.on_for_degrees(speed=-15,degrees=90)
    DriveBase.on_for_rotations(steering=0,speed=50,rotations=-6)