import RPi.GPIO as GPIO
import time
import os
import random

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

while True:
    time.sleep(2)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "ON" if current_state else "OFF"
        #print("GPIO pin %s is %s" % (sensor, new_state))
    if (current_state == True):
        randomfile = random.choice(os.listdir("/home/pi/seinfeld/"))
        file= '/home/pi/seinfeld/'+ randomfile
        os.system ('ogg123 -q '+ file)

sleep(0.1);
