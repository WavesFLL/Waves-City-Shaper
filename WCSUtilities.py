#!/usr/bin/env micropython


#utility functions used in our WCS challeng code to simplify coding robot motion

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
    return min(max_val, max(min_val, val))