#!/usr/bin/env micropython 
#Change the above to "micropython" for more speed, and "python3" for more functions

#The basic bridge code.
#Obviously it is not complete. It just turns the attachment wheels at the same rate of travel as the main wheels
#The import functions are included, so you can run this as a standalone program for testing.
#They can be removed when you integrate this with the master program.
#Bear in mind that you have already used all your buttons for the master, so you may have to use the center button as a hotkey.
#Good luck! If the wheels turn the wrong way, use a -1 somewhere or turn the attachment the other way.

from ev3dev2.motor import *
from time import sleep
DriveBase = MoveSteering(OUTPUT_B, OUTPUT_C, motor_class = MediumMotor)
Arm = LargeMotor(OUTPUT_A)
Pusher = MediumMotor(OUTPUT_D)

#Large wheel circumfrence: 216mm
#small wheel: 176mm
BigRPM = -60
BigRotations = 4
#Mulitiply the main robot's wheel RPM and distance by 2.4 to get the attachment wheel RPM and distance
SmallRPM = BigRPM*2.4
SmallRotations = BigRotations*2.4

# #beginning of the code
# Arm.off(brake=True)
# DriveBase.on_for_rotations(0, -75, 2, brake=True)
# Arm.on_for_degrees(10,100,brake=False)
# time.sleep(1)
# Pusher.on_for_rotations(SpeedRPM(SmallRPM), SmallRotations, brake=True, block=False)
# DriveBase.on_for_rotations(0, SpeedRPM(BigRPM), BigRotations, brake=True)

# Drives backwards, turns to go to bridge
Arm.on_for_degrees(10, -90, brake=True)
DriveBase.on_for_rotations(0, -40, 6.99999999999999999999999)
DriveBase.on_for_rotations(-100, 15, 0.94)
DriveBase.on_for_rotations(0, -25, 0.3)
Arm.on_for_degrees(10, -90, brake=True)


Arm.off(brake=True)
DriveBase.on_for_rotations(0, -75, 2, brake=True)
Arm.on_for_degrees(10,100,brake=False)
time.sleep(1)
Pusher.on_for_rotations(SpeedRPM(SmallRPM), SmallRotations, brake=True, block=False)
DriveBase.on_for_rotations(0, SpeedRPM(BigRPM), BigRotations, brake=True)