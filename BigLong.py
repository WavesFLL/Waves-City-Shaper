#!/usr/bin/env micropython

from time import sleep
import WCSUtilities as WSCUtil
#BigLong is Traffic Jam and TheStick merged into one


def BigLong(DriveBase,Arm,Pusher,CSL,CSR,USS,Btn,CMotSens,BMotSens,BtnUsed): #The last program which does swing, safety factor, and elevator
    