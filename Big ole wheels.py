#!/usr/bin/env micropython 
#Change the above to "micropython" for more speed, and "python3" for more functions

#The basic bridge code.
#Obviously it is not complete. It just turns the attachment wheels at the same rate of travel as the main wheels
#The import functions are included, so you can run this as a standalone program for testing.
#They can be removed when you integrate this with the master program.
#Bear in mind that you have already used all your buttons for the master, so you may have to use the center button as a hotkey.
#Good luck! If the wheels turn the wrong way, use a -1 somewhere or turn the attachment the other way.

#Import functions
from ev3dev2.motor import * #Motors, for moving
from time import sleep #Timers, for waiting
from ev3dev2.sensor.lego import ColorSensor #Sensors, for sensing
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2 #Ports, for sensors to be plugged into
from ev3dev2.button import * #Buttons, for Master program control
from ev3dev2.led import *


#Define motors and sensors
Arm = LargeMotor(OUTPUT_A) #Up and down motion
DriveBase = MoveSteering(OUTPUT_B,OUTPUT_C, motor_class=MediumMotor) #Driving
Pusher = MediumMotor(OUTPUT_D) #Out and in and rotating motions
CSL = ColorSensor(INPUT_1) #Color sensors
CSR = ColorSensor(INPUT_2) #Color sensors
USS = UltrasonicSensor() #Ultrasonic sensor
Lights = Leds()
#Defines buttons
Btn = Button()
#Defines sensing motors
CMotSens = MediumMotor(OUTPUT_C)
BMotSens = MediumMotor(OUTPUT_B)
Lights.all_off()



import WCSUtilities as WSCUtil
#Large wheel circumfrence: 216mm
#small wheel: 176mm
BigRPM = -60
BigRotations = 4
#Mulitiply the main robot's wheel RPM and distance by 2.4 to get the attachment wheel RPM and distance
SmallRPM = BigRPM*2.4
SmallRotations = BigRotations*2.4
#Puts arm up so wheels dont drag against the mat
Arm.on_for_degrees(speed=30,degrees=-85)
#Drives out of base East untill the left color sensor sees white
WSCUtil.Smooth(DriveBase, BMotSens, steerings=0,speedie=85,revolutions=5)


DriveBase.on(steering=0,speed=25)
sleep(0.25)
while(CSL.reflected_light_intensity < 80): pass
DriveBase.off()
sleep(0.2)
DriveBase.on(steering=-50, speed=10)

while(CSR.reflected_light_intensity > 20): pass
DriveBase.off
# Does "Align" with a line again. Where it makes both color sensors on the same plane
DriveBase.on(steering=50,speed=-10)
while(CSL.reflected_light_intensity < 60): pass
DriveBase.on(steering=-50,speed=-10)
while(CSR.reflected_light_intensity < 60): pass
DriveBase.on(steering=50,speed=10)
while(CSL.reflected_light_intensity > 20): pass
DriveBase.on(steering=-50, speed=10)
while(CSR.reflected_light_intensity > 20): pass
DriveBase.off()

DriveBase.on_for_rotations(steering=0, speed=20, rotations=0.5)
sleep(0.5)
DriveBase.on(steering=100,speed=-20)
while(CSL.reflected_light_intensity > 20): pass
while(CSL.reflected_light_intensity < 80): pass
DriveBase.off()
#PID
while(CSR.reflected_light_intensity > 20):
    DriveBase.on(steering=WSCUtil.constrain(WSCUtil.PID(45, CSL.reflected_light_intensity, Kp=0.5,Ki=0.01,Kd=0.2,Kg=-1, looptime=0.02), -100, 100), speed=25)

