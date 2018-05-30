# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 21:23:15 2018

@author: ccgar
"""

# testing feedback 360 serving to get the steering angle or the car

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pulse_starttime = time.time()
pulse_endtime = pulse_starttime
pulse_width = pulse_endtime - pulse_starttime
pulse_pin = 17

# GPIO 23 set up as input. It is pulled up to stop false signals  
GPIO.setup(pulse_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
print('GPIO: ', GPIO.input(pulse_pin))

def rising_callback(channel):
    print('Rising edge detected')
    pulse_width = 0
    pulse_starttime = time.time()
    while GPIO.input(channel)==1:
        pass
    pulse_endtime = time.time()
    pulse_width = pulse_endtime - pulse_starttime
    print('Pulse width: ', pulse_width)

def getpulse():
    unitsFC = 360      #Units in a full circle
    dutyScale = 1000   #Scale duty cycle to 1/1000ths
    dcMin = 29         #Minimum duty cycle
    dcMax = 971  
    pulses = []
    print('Pulse widths:', pulses)
    for i in range(0,50):
        GPIO.wait_for_edge(pulse_pin, GPIO.RISING) 
        hi_starttime = time.time()
        while GPIO.input(pulse_pin)==1:
            pass
        hi_endtime = time.time()
        tHigh = hi_endtime - hi_starttime
        
        low_starttime = hi_endtime
        while GPIO.input(pulse_pin)==0:
            pass
        low_endtime = time.time()
        tLow = low_endtime - low_starttime
        dc = (dutyScale * tHigh) / (tHigh + tLow);      
        pulses.append(dc)
        
    dc = sum(pulses)/len(pulses)
    theta = (unitsFC - 1) - ((dc - dcMin) * unitsFC) / (dcMax - dcMin + 1)
    print('pulses {} {}'.format(round(dc,0), round(theta,0)))
        
print("Waiting for the rising edge")
#GPIO.add_event_detect(pulse_pin, GPIO.RISING, callback=rising_callback)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
i=0
while True:
    try:
        print('looping: ', i)
        print('GPIO: ', GPIO.input(pulse_pin))
        print('Pulse width 1: ', pulse_width)
        getpulse() 
        time.sleep(0.3)
        i+=1
    except KeyboardInterrupt:  
        GPIO.cleanup() 
GPIO.cleanup()
    