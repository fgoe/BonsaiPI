#!/usr/bin/env python

# Setup
#--------------------------------------

#Imports
import RPi.GPIO as GPIO
import time
import select
import sys
VWC=0

#VWC to switch pump on
VWCthres=45

#Time that the pump is running
pumpTime=12

#Sleep for other scripts to finish
time.sleep(1.0)



# Main
#---------------------------------------

#Print threshold
print ("VWC Threshold: %.3f" % VWCthres)

#read value from file in /tmp
valuefile = open('/tmp/VWCvalue','r')
VWC = valuefile.readline()
VWCfloat = float(VWC)
valuefile.close()
print ("VWC Value from File: %.3f" % VWCfloat)

#check variable type
if 0 < VWCfloat >= 99:
   sys.exit()

#Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

#If VWC is too low, switch on pump for VWCthres seconds
if VWCfloat < VWCthres:
 print ("Tree needs water\n")
 GPIO.output(11, True)
 time.sleep(pumpTime)
 GPIO.output(11, False)
if VWCfloat > VWCthres:
 print ("Tree does not need water\n")




#cleanup after code is done and exit
#---------------------------------------

GPIO.cleanup()
sys.exit()
