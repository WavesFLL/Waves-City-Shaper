#!/usr/bin/env micropython

from time import sleep #Timers, for waiting
import WCSUtilities as WSCUtil
from ev3dev2.motor import * #Motors, for moving
from time import sleep #Timers, for waiting
from ev3dev2.sensor.lego import ColorSensor #Sensors, for sensing
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2 #Ports, for sensors to be plugged into
from ev3dev2.button import * #Buttons, for Master program control
from ev3dev2.led import *


Arm = LargeMotor(OUTPUT_A) #Up and down motion
DriveBase = MoveSteering(OUTPUT_B,OUTPUT_C, motor_class=MediumMotor) #Driving
TankBase = MoveTank(OUTPUT_B,OUTPUT_C, motor_class=MediumMotor)
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
#Large wheel circumfrence: 216mm
#small wheel: 176mm
BigRPM = 60
BigRotations = 3.5
#Mulitiply the main robot's wheel RPM and distance by 2.4 to get the attachment wheel RPM and distance
SmallRPM = BigRPM*-2.4
SmallRotations = BigRotations*2.4

#Arm.on_for_degrees(speed=25,degrees=-85)

#while(1):
    #DriveBase.on(steering=WSCUtil.constrain(WSCUtil.PID(45, CSL.reflected_light_intensity, Kp=0.5,Ki=0.01,Kd=0.2,Kg=-1, looptime=0.02), -100, 100), speed=25)
Arm.on_for_degrees(75,15)
Pusher.on_for_rotations(SpeedRPM(SmallRPM), SmallRotations, brake=True, block=False)
DriveBase.on_for_rotations(0, SpeedRPM(BigRPM), BigRotations, brake=True, block=False)
sleep(2.5)
Arm.off(brake=False)
sleep(5)
