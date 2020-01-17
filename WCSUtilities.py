#!/usr/bin/env micropython

from time import time
#utility functions used in our WCS challeng code to simplify coding robot motion
integral = 0
pasterror = 0
LT = 0
returnVar = 0
#Moving smooth 
def Smooth(DriveBase,MOTSENS,steerings,speedie,revolutions):
    MotSensVar = MOTSENS.position
    DriveBase.on(steering=steerings, speed=speedie)
    while(MOTSENS.position<= (360*revolutions)+MotSensVar):
        pass
# no need for Smooth_B since the MOTSENS object is now passed in
#def Smooth_B(steerings,speedie,revolutions,Drivebase,BMOTSENS): 
#    MotSensVar = BMOTSENS.position
#    DriveBase.on(steering=steerings, speed=speedie)
#    while(BMOTSENS.position<= (360*revolutions)+MotSensVar):
#        pass
def RotInches(DriveBase,steer,speedie,millimeters):
    DriveBase.on_for_rotations(steering=steer,speed=speedie,rotations=millimeters/176)
def constrain(val, min_val, max_val):
    if val == None:
        val = 0
    return min(max_val, max(min_val, val))




def PID(target,feedback,Kp = 1,Ki = 0,Kd = 0,Kg = 1,looptime = 0.01):
#Returns a float value containing the output of the PID controller

    global returnVar
    global LT
    if(time() - LT >= looptime):
        
        global integral
        global pasterror
        error = target - feedback
        proportional = error
        integral = integral + error

        derivative = error - pasterror 

        pasterror = error
        LT = time()
        returnVar = ((proportional * Kp) + (integral * Ki) + (derivative * Kd))*Kg
    return returnVar
        
