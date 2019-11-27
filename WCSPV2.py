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

<<<<<<< HEAD
    Smooth_B(steerings=20,speedie=25,revolutions=1.25) #Drives toward black line
    
    #Follows said line with the right color sensor, 
    #until left color sensor sees the edge of launch area
    while(CSL.reflected_light_intensity >= 30): 
        error = (45 - CSR.reflected_light_intensity)*0.9
        DriveBase.on(error, speed=22)
    DriveBase.off()

    #Drives forward slightly, so that left color sensor can follow black line South of Crane
    DriveBase.on_for_rotations(steering=-50,speed=22,rotations=0.75)
    Smooth_C(steerings=0,speedie=30,revolutions=0.15)

    # Follows line up to crane with left sensor
    # ...until right color sensor sees white
    while(CSR.reflected_light_intensity < 65): 
        error = (35 - CSL.reflected_light_intensity)*0.9
        DriveBase.on(steering=error,speed=22)
    DriveBase.off()

    #Maneuvers around crane
    DriveBase.on_for_rotations(steering=0,speed=-7,rotations=0.2)
    DriveBase.on_for_rotations(steering=100,speed=7,rotations=0.15)
    DriveBase.on_for_rotations(steering=0,speed=7,rotations=0.27)
    DriveBase.on_for_rotations(steering=-100,speed=20,rotations=0.9)

    #Lifts arm up and down 15 times
    for i in range(22):
        Arm.on_for_degrees(speed=-10,degrees=18)
        Arm.on_for_degrees(speed=20,degrees=18)

    #Unhooks from Crane and drives back to home
    DriveBase.on_for_rotations(steering=-100,speed=-30,rotations=0.25)
    DriveBase.on_for_rotations(steering=0,speed=-50,rotations=0.5)
    DriveBase.on_for_rotations(steering=-15,speed=-60,rotations=4.5)
    DriveBase.on_for_rotations(steering=100,speed=30,rotations=0.5)
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
=======
def Cake (): #Fourth program takes the cake to a circle
    #Waits for us to move our hands
    time.sleep(0.5)
    #Drives foward to put Cake in a circle
    DriveBase.on_for_rotations(steering=0,speed=30,rotations=2.25)
    #Drives back to home
    DriveBase.on_for_rotations(steering=-10,speed=50,rotations=-6) 
>>>>>>> BreakCodeInToFiles
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