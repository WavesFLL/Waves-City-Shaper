#!/usr/bin/env micropython

def Cake (): #Fourth program takes the cake to a circle
    #Waits for us to move our hands
    time.sleep(0.5)
    #Drives foward to put Cake in a circle
    DriveBase.on_for_rotations(steering=0,speed=30,rotations=2.25)
    #Drives back to home
    DriveBase.on_for_rotations(steering=-10,speed=50,rotations=-6) 
