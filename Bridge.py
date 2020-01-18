#!/usr/bin/env micropython 
#Change the above to "micropython" for more speed, and "python3" for more functions

#The basic bridge code.
#Obviously it is not complete. It just turns the attachment wheels at the same rate of travel as the main wheels
#The import functions are included, so you can run this as a standalone program for testing.
#They can be removed when you integrate this with the master program.
#Bear in mind that you have already used all your buttons for the master, so you may have to use the center button as a hotkey.
#Good luck! If the wheels turn the wrong way, use a -1 somewhere or turn the attachment the other way.
import WCSUtilities as WSCUtil
#Import functions
from ev3dev2.motor import * #Motors, for moving
from time import sleep #Timers, for waiting
from ev3dev2.sensor.lego import ColorSensor #Sensors, for sensing
from ev3dev2.sensor.lego import UltrasonicSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2 #Ports, for sensors to be plugged into
from ev3dev2.button import * #Buttons, for Master program control
from ev3dev2.led import *


#Define motors and sensors
'''Arm = LargeMotor(OUTPUT_A) #Up and down motion
DriveBase = MoveSteering(OUTPUT_B,OUTPUT_C, motor_class=MediumMotor) #Driving
Pusher = MediumMotor(OUTPUT_D) #Out and in and rotating motions
CSL = ColorSensor(INPUT_1) #Color sensors
CSR = ColorSensor(INPUT_2) #Color sensors
USS = UltrasonicSensor() #Ultrasonic sensor
GYRO = GyroSensor()
Lights = Leds()
#Defines buttons
Btn = Button()
#Defines sensing motors
CMotSens = MediumMotor(OUTPUT_C)
BMotSens = MediumMotor(OUTPUT_B)'''


def Bridge(Arm,DriveBase,Pusher,CSL,CSR,USS,Btn,CMotSens,BMotSens,Lights):
    Lights.all_off()
    Arm.on_for_degrees(speed=10, degrees=-15)
    MotSensVar = CMotSens.position
        #Follows the wall out of base
    while(CMotSens.position<= (360*1.5)+MotSensVar):
        error = (29.6 - USS.distance_centimeters)*10
        error = WSCUtil.constrain(error,-100,100)
        error = 0 - error
        DriveBase.on(steering=error,speed=30) 
    #Starts following line os as not interfered with traffic jam
    while(CSL.reflected_light_intensity > 50):
        error = (29.6 - USS.distance_centimeters)*10
        error = WSCUtil.constrain(error,-100,100)
        error = 0 - error
        DriveBase.on(steering=error,speed=30) 
    MotSensVar = CMotSens.position
    #Follows wall to re align
    while(CMotSens.position<= (360*1.5)+MotSensVar):
        error = (29.6 - USS.distance_centimeters)*10
        error = WSCUtil.constrain(error,-100,100)
        error = 0 - error
        DriveBase.on(steering=error,speed=30) 
    MotSensVar = CMotSens.position
    Arm.on_for_degrees(speed=10,degrees=-80, block=False)
    #Follows line around small curve

    while(CMotSens.position < (360*1.75)+MotSensVar):
        DriveBase.on(steering=(45-CSR.reflected_light_intensity)*-0.8,speed=30)

    while(CSL.reflected_light_intensity<80): 
        DriveBase.on(steering=(45-CSR.reflected_light_intensity)*-1.5,speed=15)  

    while(CSL.reflected_light_intensity>20): 
        DriveBase.on(steering=(45-CSR.reflected_light_intensity)*-2,speed=15) 
        
    DriveBase.off()

    DriveBase.on_for_rotations(steering=0,speed=15,rotations=0.6)
    DriveBase.on_for_rotations(steering=-100,speed=20, rotations=0.21)
    DriveBase.on(steering=-100,speed=20)
    while(CSL.reflected_light_intensity > 20): pass
    DriveBase.on(steering=-100,speed=20)
    while(CSL.reflected_light_intensity < 70): pass
    MotSensVar = BMotSens.position
    while(BMotSens.position < (360*1.5)+MotSensVar): 
        DriveBase.on(steering=(55-CSL.reflected_light_intensity)*-0.8,speed=25)
    while(CSR.reflected_light_intensity > 20): 
        DriveBase.on(steering=(45-CSL.reflected_light_intensity)*-0.9,speed=15)
    DriveBase.off()
    DriveBase.on_for_rotations(steering=-50,speed=-20,rotations=1.2)
    DriveBase.on_for_rotations(steering=100,speed=15,rotations=0.8)
    Arm.off(brake=False)
    sleep(1)
    Arm.on_for_degrees(75,20)
    #Large wheel circumfrence: 216mm
    #small wheel: 176mm
    BigRPM = -60
    BigRotations = 4.2
    #Mulitiply the main robot's wheel RPM and distance by 2.4 to get the attachment wheel RPM and distance
    SmallRPM = BigRPM*-2.4
    SmallRotations = BigRotations*2.4
    Pusher.on_for_rotations(SpeedRPM(SmallRPM), SmallRotations, brake=True, block=False)
    DriveBase.on_for_rotations(0, SpeedRPM(BigRPM), BigRotations, brake=True, block=False)
    sleep(1.7)
    Arm.off(brake=False)
    sleep(5)