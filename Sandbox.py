#!/usr/bin/env micropython

from time import sleep #Timers, for waiting
import WCSUtilities as WSCUtil

def PIDtest(DriveBase,Lights,Arm,Pusher,CSR): 
    while True:
       DriveBase.on(steering=WSCUtil.PID(50, CSR.reflected_light_intensity,Kp=1, Ki=0, Kd=0),speed=30)
    
