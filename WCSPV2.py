#!/usr/bin/env micropython
#Change the language to "micropython" for more speed, and "python3" for more functionality

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
CMOTSENS = MediumMotor(OUTPUT_C)
BMOTSENS = MediumMotor(OUTPUT_B)

#Moving smooth
def Smooth_C(steerings,speedie,revolutions):
    MotSensVar = CMOTSENS.position
    DriveBase.on(steering=steerings, speed=speedie)
    while(CMOTSENS.position<= (360*revolutions)+MotSensVar):
        pass
def Smooth_B(steerings,speedie,revolutions): 
    MotSensVar = BMOTSENS.position
    DriveBase.on(steering=steerings, speed=speedie)
    while(BMOTSENS.position<= (360*revolutions)+MotSensVar):
        pass
def RotInches(steerin,speedie,millimeters):
    DriveBase.on_for_rotations(steering=steerin,speed=speedie,rotations=millimeters/176)
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

<<<<<<< refs/remotes/origin/BreakCodeInToFiles
def StuffInCircle(): #Our first program which does architecture and starts crane
    time.sleep(0.5) #Waits for 0.5 seconds so we can remove our hands
    Lights.all_off() #Turns all lights off
    Arm.on_for_degrees(speed=10,degrees=-25) #lifts arm slightly so the robot can sstart moving
    DriveBase.on_for_rotations(steering=0,speed=30,rotations=2.2) #Drives forward to get out of base
    Arm.on_for_degrees(speed=5,degrees=25) #lowers arm
    time.sleep(1)
    Pusher.on_for_rotations(speed=100,rotations=-7.35,block=True) #Moves the pusher out
    DriveBase.on(steering=0,speed=30) #Drives forward...
    while(CSR.color != CSR.COLOR_BLUE): # ...until the color sensor sees blue
        pass

    DriveBase.stop()
    Lights.animate_police_lights('RED', 'GREEN', sleeptime=0.05, duration=0, block=False)
    Pusher.on_for_rotations(speed=100,rotations=1) #Pulls pusher in, so it's not touching blue block
    Arm.on_for_degrees(speed=100,degrees=-90, block=False) #Lifts up arm
    DriveBase.on_for_rotations(steering=-25,speed=-90,rotations=4) #Drives back to home
    DriveBase.on_for_rotations(steering=0,speed=50,rotations=-1)
    time.sleep(2)
=======
def Crane(): #The second program, finishes crane
    time.sleep(0.5) #Waits for us to move our hands
    #Makes sure it knows where the arm is
    Arm.on(-10)
    Arm.wait_until_not_moving(timeout=3000)
    Arm.off(brake=True)
    Arm.on_for_degrees(speed=25,degrees=30, block=False)
>>>>>>> moved stuff in circle software

def Cake (): #Fourth program takes the cake to a circle
    #Waits for us to move our hands
    time.sleep(0.5)
    #Drives foward to put Cake in a circle
    DriveBase.on_for_rotations(steering=0,speed=30,rotations=2.25)
    #Drives back to home
    DriveBase.on_for_rotations(steering=-10,speed=50,rotations=-6) 
def TheStick(): #The last program which does swing, safety factor, and elevator
    #Makes sure rotator is in right spot
    Pusher.run_direct(duty_cycle_sp = 30)
    Pusher.wait_until_not_moving(timeout=3000)
    Pusher.off(brake=True)
    Pusher.on_for_degrees(speed=25,degrees=-80)
    Btn.wait_for_bump('enter')
    time.sleep(1)
    MotSensVar = CMOTSENS.position
    #Alternates following the wall and the line
    while(CMOTSENS.position<= (360*1.5)+MotSensVar):
        error = (29.6 - USS.distance_centimeters)*10
        error = constrain(error,-100,100)
        error = 0 - error
        DriveBase.on(steering=error,speed=30) 
    while(CSL.reflected_light_intensity > 50):
        error = (29.6 - USS.distance_centimeters)*10
        error = constrain(error,-100,100)
        error = 0 - error
        DriveBase.on(steering=error,speed=30) 
    MotSensVar = CMOTSENS.position
    while(CMOTSENS.position<= (360*1.5)+MotSensVar):
        error = (29.6 - USS.distance_centimeters)*10
        error = constrain(error,-100,100)
        error = 0 - error
        DriveBase.on(steering=error,speed=30) 
    MotSensVar = CMOTSENS.position
    while(CMOTSENS.position< (360*1.75)+MotSensVar):
        DriveBase.on(steering=(45-CSR.reflected_light_intensity)*-1,speed=30)

    while(CSL.reflected_light_intensity<80): 
        DriveBase.on(steering=(45-CSR.reflected_light_intensity)*-2,speed=15)  

    while(CSL.reflected_light_intensity>20): 
        DriveBase.on(steering=(45-CSR.reflected_light_intensity)*-2,speed=15) 
     
    MotSensVar = CMOTSENS.position
    while(CMOTSENS.position< (360*1)+MotSensVar):
        DriveBase.on(steering=(45-CSR.reflected_light_intensity)*-1.25,speed=15)
    DriveBase.off()
    #Puts rotator down and drives foward to do swing
    Pusher.on_for_degrees(speed=30,degrees=260)

    MotSensVar = CMOTSENS.position
    while(CMOTSENS.position< (360*0.75)+MotSensVar):
        DriveBase.on(steering=(45-CSR.reflected_light_intensity)*-1.25,speed=15)
    DriveBase.off()

    #Manuvers around to get the two SouthWest beams knocked down
    DriveBase.on_for_rotations(steering=-100,speed=10,rotations=0.15)
    Pusher.on_for_degrees(speed=100,degrees=-470)
    DriveBase.on_for_rotations(steering=0,speed=10,rotations=0.3)
    DriveBase.on_for_rotations(steering=-50,speed=-30,rotations=0.6)
    Arm.on_for_degrees(speed=75,degrees=-90)
    DriveBase.on_for_rotations(steering=100,speed=25,rotations=0.25)
    #Drives backward till the left color sensor sees the black line running north east.
    DriveBase.on_for_rotations(steering=0,speed=-20,rotations=1.5)
    DriveBase.on(steering=0,speed=-20)
    while(CSL.reflected_light_intensity > 20): pass
    DriveBase.off()
    DriveBase.on_for_rotations(steering=-100,speed=15,rotations=0.5)
    Pusher.on_for_degrees(speed=100,degrees=150,block=False)
    DriveBase.on_for_rotations(steering=0,speed=40,rotations=1.5)
    DriveBase.on_for_rotations(steering=-100,speed=20,rotations=0.6)
    Arm.on_for_degrees(speed=10,degrees=10,block=False)
    Pusher.on_for_degrees(speed=-100, degrees=1080)
    time.sleep(1)
    DriveBase.on_for_rotations(steering=0,speed=100,rotations=-1)

while True: #Master program which runs different programs depending on which button is pushed
    DriveBase.off(brake=False)
    Arm.off(brake=False)
    Pusher.off(brake=False)
    Lights.all_off()
    if(Btn.left):
       StuffInCircle()
    if(Btn.up):
        Crane()
    if(Btn.right): 
        Alift()
    if(Btn.down):
        Cake()
    if(Btn.enter):
        TheStick()