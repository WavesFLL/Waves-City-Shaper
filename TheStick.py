#!/usr/bin/env micropython
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