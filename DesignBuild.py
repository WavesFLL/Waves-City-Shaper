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
from time import sleep #Timers, for waiting
def DesignBuild(DriveBase,Lights,Arm,Pusher,CSR):
    #Define motors and sensors


    #Our first program which does architecture drops crane
    sleep(0.5) #Waits for 0.5 seconds so we can remove our hands
    Lights.all_off() #Turns all lights off
    Arm.on_for_degrees(speed=10,degrees=-25) #lifts arm slightly so the robot can start moving
    DriveBase.on_for_rotations(steering=0,speed=30,rotations=2.2) #Drives forward to get out of base
    Arm.off(brake=False) #lowers arm
    sleep(1)
    Pusher.off()
    Pusher.on_for_rotations(speed=100,rotations=-3.625,block=True) #Moves the pusher out
    DriveBase.on(steering=0,speed=30) #Drives forward...
    while(CSR.color != CSR.COLOR_BLUE): # ...until the color sensor sees blue
        pass

    DriveBase.stop()
    Lights.animate_police_lights('RED', 'GREEN', sleeptime=0.05, duration=0, block=False)
    Pusher.on_for_rotations(speed=100,rotations=3.6) #Pulls pusher in, so it's not touching crane
    Arm.on_for_degrees(speed=100,degrees=-90, block=False) #Lifts up arm
    DriveBase.on_for_rotations(steering=0,speed=-40, rotations=0.75)#Drives back to base
    DriveBase.on_for_rotations(steering=-25,speed=-40,rotations=2.5)
    DriveBase.on_for_rotations(steering=0,speed=-50,rotations=1)
    sleep(2)
