#!/usr/bin/env micropython

def Alift (): #Third program does Traffic jam
   time.sleep(0.5) #Waits for us to move our hands
   #Drives straight while following wall until the right color sensor sees blue
   while (CSR.color != 2): 
        error = (11 - USS.distance_centimeters)*10
        error = constrain(error,-100,100)
        error = 0 - error
        DriveBase.on(steering=error,speed=30)
   #Manuvers to get traffic jam
   RotInches(steerin=0, speedie=30,millimeters=130)
   DriveBase.on_for_rotations(steering=100,speed=30,rotations=0.1)
   #Rotates are to lift traffic jam
   Pusher.on_for_degrees(speed=25,degrees=450)
   #Waits for two seconds to make sure the traffic jam is cleared
   time.sleep(2)
   #Rotates arm down and drives back to home
   Pusher.on_for_degrees(speed=100,degrees=-300)
   Arm.on_for_degrees(speed=-5,degrees=90,block=False)
   DriveBase.on_for_rotations(steering=0,speed=-90,rotations=5.5)