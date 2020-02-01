#!/usr/bin/env micropython

from time import sleep #Timers, for waiting

def StuffInCircle(DriveBase,Lights,Arm,Pusher,CSR): #Our first program which does architecture and starts crane
    sleep(0.5) #Waits for 0.5 seconds so we can remove our hands
    Lights.all_off() #Turns all lights off
    Arm.on_for_degrees(speed=10,degrees=-25) #lifts arm slightly so the robot can sstart moving
    DriveBase.on_for_rotations(steering=0,speed=30,rotations=2.2) #Drives forward to get out of base
    Arm.on_for_degrees(speed=5,degrees=25) #lowers arm
    sleep(1)
    Pusher.on_for_rotations(speed=100,rotations=-7.35,block=True) #Moves the pusher out
    DriveBase.on(steering=0,speed=30) #Drives forward...
    while(CSR.color != CSR.COLOR_BLUE): # ...until the color sensor sees blue
        pass

    DriveBase.stop()
    Lights.animate_police_lights('RED', 'GREEN', sleeptime=0.05, duration=0, block=False)
    Pusher.on_for_rotations(speed=100,rotations=1) #Pulls pusher in, so it's not touching blue block
    Arm.on_for_degrees(speed=100,degrees=-90, block=False) #Lifts up arm
    Arm.on_for_degrees(speed=100,degrees=-90, block=False) #Lifts up arm
    DriveBase.on_for_rotations(steering=0,speed=-40, rotations=0.75)
    DriveBase.on_for_rotations(steering=-25,speed=-40,rotations=2.5)
    DriveBase.on_for_rotations(steering=0,speed=-50,rotations=1)
    sleep(2)
