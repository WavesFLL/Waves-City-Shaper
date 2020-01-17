#!/usr/bin/env micropython

from time import sleep

def Cake(DriveBase): #Fourth program takes the cake to a circle
    #Waits for us to move our hands
    sleep(0.5)
    #Drives foward to put Cake in a circle
    DriveBase.on_for_rotations(steering=0,speed=30,rotations=2.25)
    #Drives back to home
    DriveBase.on_for_rotations(steering=-10,speed=90,rotations=-6) 
