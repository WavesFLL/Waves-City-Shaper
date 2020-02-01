#!/usr/bin/env micropython

from time import sleep
import WCSUtilities as WCSUtil
#BigLong is Traffic Jam and TheStick merged into one


def BigLong(DriveBase,Arm,Pusher,CSL,CSR,USS,Btn,CMotSens,BMotSens,BtnUsed): #The last program which does swing, safety factor, and elevator
    
    #Makes sure rotator is in right spot
    Pusher.run_direct(duty_cycle_sp = 30)
    Pusher.wait_until_not_moving(timeout=3000)
    Pusher.off(brake=True)
    Pusher.on_for_degrees(speed=25,degrees=-340) #Needs to be 80 left of 0 for the rest of TheStick
    Btn.wait_for_bump(BtnUsed)
    sleep(1)    #Waits for us to move our hands

    #----------------------# ALIFT CODE

    #Drives straight while following wall until the right color sensor sees blue
    while (CSR.color != 2): 
        error = (11.1 - USS.distance_centimeters)*10
        error = WCSUtil.constrain(error,-100,100)
        error = 0 - error
        DriveBase.on(steering=error,speed=35)
    #Manuvers to get traffic jam
    WCSUtil.RotInches(DriveBase,steer=0,speedie=30,millimeters=130)
    DriveBase.on_for_rotations(steering=100,speed=30,rotations=0.1)
    
    #Rotates arm to lift traffic jam
    MotSensVar = Pusher.position
    Pusher.on_for_degrees(speed=25,degrees=450, block = False)
    while(Pusher.position < 50+MotSensVar): pass
    DriveBase.on_for_rotations(steering=0,speed=5,rotations=0.1)
    Arm.on_for_degrees(speed=-4, degrees=50)
    
    
    Pusher.on_for_degrees(speed=50, degrees=-190, block=False)
    
    DriveBase.on_for_rotations(steering=0,speed=-25,rotations=0.5)
    DriveBase.on(steering=-50,speed=25)
    while(CSR.color != CSR.COLOR_BLACK): pass
    DriveBase.on(steering=0,speed=25)
    while(CSR.color != CSR.COLOR_WHITE): pass
   
    #Follows line to get to swing
    WCSUtil.Smooth(DriveBase,BMotSens,steerings = 0, speedie =25, revolutions=0.3)
    DriveBase.on(steering = 50, speed =25)
    while(CSR.color != CSR.COLOR_BLACK): pass

    MotSensVar = CMotSens.position
    while(CMotSens.position< (360*0.5)+MotSensVar):
        DriveBase.on(steering=(45-CSR.reflected_light_intensity)*-1.5,speed=20)
    MotSensVar = CMotSens.position
    while(CMotSens.position< (360*0.7)+MotSensVar):
        DriveBase.on(steering=(45-CSR.reflected_light_intensity)*-0.5,speed=40)
    Arm.off(brake = False)

    while(CSL.reflected_light_intensity<80):   
        error = (29.6 - USS.distance_centimeters)*8 #10
        error = WCSUtil.constrain(error,-100,100)
        error = 0 - error
        DriveBase.on(steering=error,speed=40)
    
    while(CSL.reflected_light_intensity>20): 
        error = (29.6 - USS.distance_centimeters)*8 #10
        error = WCSUtil.constrain(error,-100,100)
        error = 0 - error
        DriveBase.on(steering=error,speed=40)
    MotSensVar = CMotSens.position
    
    while(CMotSens.position< (360*1)+MotSensVar):
        DriveBase.on(steering=(45-CSR.reflected_light_intensity)*-1.25,speed=15)
    DriveBase.off()
    #Puts rotator down and drives foward to do swing
    Pusher.on_for_degrees(speed=30,degrees=260)

    MotSensVar = CMotSens.position
    while(CMotSens.position< (360*0.75)+MotSensVar):
        DriveBase.on(steering=(45-CSR.reflected_light_intensity)*-1.25,speed=15)
    DriveBase.off()

    #Manuvers around to get the two SouthWest beams knocked down
    DriveBase.on_for_rotations(steering=-100,speed=10,rotations=0.15)
    Pusher.on_for_degrees(speed=100,degrees=-470)
    DriveBase.on_for_rotations(steering=0,speed=10,rotations=0.35)
    DriveBase.on_for_rotations(steering=-50,speed=-30,rotations=0.6)
    Arm.on_for_degrees(speed=75,degrees=-90)
    DriveBase.on_for_rotations(steering=100,speed=25,rotations=0.25)
    #Drives backward till the left color sensor sees the black line running north east.
    DriveBase.on_for_rotations(steering=0,speed=-20,rotations=1.5)
    DriveBase.on(steering=0,speed=-20)
    while(CSL.reflected_light_intensity > 20): pass
    DriveBase.off()

    # "Aligns" with the line by turning untill both color sensors are horizontal to the line
    DriveBase.on(steering=-50, speed=-10)
    while(CSR.reflected_light_intensity > 20): pass
    DriveBase.off
    DriveBase.on(steering=50,speed=10)
    while(CSL.reflected_light_intensity < 60): pass
    DriveBase.off()
    DriveBase.on(steering=-50,speed=10)
    while(CSR.reflected_light_intensity < 60): pass
    DriveBase.off()
    DriveBase.on(steering=50,speed=-10)
    while(CSL.reflected_light_intensity > 20): pass
    DriveBase.off()
    DriveBase.on(steering=-50, speed=-10)
    while(CSR.reflected_light_intensity > 20): pass
    DriveBase.off()
    DriveBase.on_for_rotations(steering=0, speed=20, rotations=0.5)
    DriveBase.on(steering=100,speed=-20)
    while(CSL.reflected_light_intensity > 20): pass
    DriveBase.off()

    MotSensVar = CMotSens.position
    while(CMotSens.position< (360*0.75)+MotSensVar):
        DriveBase.on(steering=(45-CSL.reflected_light_intensity)*1,speed=15)  

    MotSensVar = CMotSens.position
    while(CMotSens.position< (360*0.25)+MotSensVar):
        DriveBase.on(steering=(45-CSL.reflected_light_intensity)*0.6,speed=15)  

    while (CSL.reflected_light_intensity < 80):
        DriveBase.on(steering=(45-CSL.reflected_light_intensity)*0.6,speed=15)  
    DriveBase.off()
    
    #Does elevator by turning to face it and swinging the arm around
    DriveBase.on_for_rotations(steering=-100, speed=10, rotations=0.55)
    DriveBase.on_for_rotations(steering=0,speed=10,rotations=0.15)
    Pusher.on_for_degrees(speed=-50, degrees=1080)
    WCSUtil.Smooth(DriveBase,BMotSens,steerings=100, speedie=20, revolutions=0.45)
    WCSUtil.Smooth(DriveBase,BMotSens,steerings=0, speedie=20, revolutions=0.6)
    DriveBase.on_for_rotations(steering=-50,speed=15,rotations=1)
    Arm.off(brake=False)
    sleep(1)
    #Maunvers around the elevator and heads North East to do tower
    MotSensVar = CMotSens.position
    while(CMotSens.position<= (360*0.8)+MotSensVar):
        error = (28.1 - USS.distance_centimeters)*10
        error = WCSUtil.constrain(error,-100,100)
        error = 0 - error
        DriveBase.on(steering=error,speed=20) 
    DriveBase.off()
    sleep(1)
    
    #Lifts up tower and holds foe three seconds so tower can stabilize
    Pusher.on_for_degrees(speed=100, degrees=250)
    sleep(2)
    Arm.on_for_degrees(speed=10,degrees=-90)
    
    #Disengages from tower and drives back to base
    DriveBase.on_for_rotations(steering=0,speed=-10,rotations=0.6)
    DriveBase.on_for_rotations(steering=-100,speed=-10,rotations=0.45)
    MotSensVar = CMotSens.position
    DriveBase.on(steering=-12,speed=-75)
    while(CMotSens.position>(360*-2.25)+MotSensVar): pass


    DriveBase.on_for_rotations(steering=0,speed=-80,rotations=9)