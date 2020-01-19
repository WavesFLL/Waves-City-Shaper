#!/usr/bin/env micropython

from time import sleep

def Cake(DriveBase): #Fourth program takes the cake to a circle
    #Waits for us to move our hands
    sleep(0.5)
    #Drives foward to put Cake in a circle
    DriveBase.on_for_rotations(steering=0,speed=40,rotations=2.25)
    #Drives back to home
    DriveBase.on_for_rotations(steering=-20,speed=85,rotations=-5.8) 
