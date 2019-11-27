#!/usr/bin/env micropython

def Crane(): #The second program, finishes crane
    time.sleep(0.5) #Waits for us to move our hands
    #Makes sure it knows where the arm is
    Arm.on(-10)
    Arm.wait_until_not_moving(timeout=3000)
    Arm.off(brake=True)
    Arm.on_for_degrees(speed=25,degrees=30, block=False)

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
