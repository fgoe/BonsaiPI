#!/usr/bin/env python
#Read Vegetronix Sensor and calculate VWC value
#Code based on "read analogue voltage on Custard Pi 2" example
# -*- coding: utf-8 -*-

#Imports
import RPi.GPIO as GPIO
import select
import time
import sys

#Set GPIO stuff
#GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(24,GPIO.OUT)    #pin23 is clock
GPIO.setup(23,GPIO.OUT)    #pin19 is data out
GPIO.setup(19,GPIO.OUT)    #pin24 is chip select 0
GPIO.setup(21,GPIO.IN)     #pin21 is data in

GPIO.output(24,True)
GPIO.output(23,False)
GPIO.output(19,True)

#set up data for ADC chip
word1= [1, 1, 0, 1, 1]

#reads analogue voltge from channel 0
while 1:
 GPIO.output(24,False)  #select channel 0
 anip=0                  #initialise variable
 VWC=0

 #set up channel 0
 for x in range (0,5):
        GPIO.output(19, word1[x])
        time.sleep(0.01)
        GPIO.output(23, True)
        time.sleep(0.01)
        GPIO.output(23, False)

 #read analogue voltage
 for x in range (0,12):
        GPIO.output(23,True)
        time.sleep(0.01)
        bit=GPIO.input(21)
        time.sleep(0.01)
        GPIO.output(23,False)
        value=bit*2**(12-x-1)
        anip=anip+value

 GPIO.output(24,True)

 volt = anip*3.3/4096
 print ("Volt: %.3f" % volt)

#Linearisation of curve parts
 if 0.1 <= volt < 1.1:
    VWC = 10*volt-1
 elif 1.1 <= volt < 1.3:
    VWC = 25*volt-17.5
 elif 1.3 <= volt < 1.82:
    VWC = 48.08*volt-47.5
 elif 1.82 <= volt < 2.2:
    VWC = 26.32*volt-7.89
 print ("VWC:  %.3f" % VWC)

#Loop till Enter is pressed
 if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = raw_input()
        break

#Cleanup after code execution
GPIO.cleanup()
sys.exit()
