from __future__ import division
import RPi.GPIO as IO
import time
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep




#//////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////SET MOTOR SPEED//////////////////////////////////////
#/////////////////////////// RANGE:  0...100[%}////////////////////////////////////
forward_speed=40#[%]
reverse_speed=60#[%]
turns_speed=85#[%]
#///////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////

#back_obscale=0
#front_obscale=0

back_obscale=False

IO.setmode(IO.BCM)
LEFT_IR=14
RIGHT_IR=3

IO.setup(LEFT_IR,IO.IN)
IO.setup(RIGHT_IR,IO.IN)

PWM_DRIVE_LEFT = 21
FORWARD_LEFT_PIN = 26
REVERSE_LEFT_PIN = 19

PWM_DRIVE_RIGHT = 5
FORWARD_RIGHT_PIN = 13
REVERSE_RIGHT_PIN = 6


# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)

# Initialise objects for H-Bridge digital GPIO pins
forwardLeft = DigitalOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = DigitalOutputDevice(REVERSE_LEFT_PIN)
forwardRight = DigitalOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = DigitalOutputDevice(REVERSE_RIGHT_PIN)


TRIG_BACK = 23
ECHO_BACK = 24

IO.setup(TRIG_BACK,IO.OUT)
IO.setup(ECHO_BACK,IO.IN)

TRIG_FRONT = 17
ECHO_FRONT = 27

IO.setup(TRIG_FRONT,IO.OUT)
IO.setup(ECHO_FRONT,IO.IN)


def allStop():
	forwardLeft.value = False
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = False
	driveLeft.value = 0
	driveRight.value = 0

def forwardDrive():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = forward_speed/100
	driveRight.value = forward_speed/100
def reverseDrive():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = reverse_speed/100
	driveRight.value = reverse_speed/100

def spinLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = forward_speed/100
	driveRight.value = forward_speed/100

def SpinRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = forward_speed/100
	driveRight.value = forward_speed/100

def forwardTurnLeft():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = turns_speed/800
	driveRight.value = turns_speed/100

def forwardTurnRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = turns_speed/100
	driveRight.value = turns_speed/800

def reverseTurnLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = turns_speed/400
	driveRight.value = turns_speed/100

def reverseTurnRight():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = turns_speed/100
	driveRight.value = turns_speed/400

def frontSensor():


	    IO.output(TRIG_FRONT, False)
	    time.sleep(0.1)
	    IO.output(TRIG_FRONT, True)
	    time.sleep(0.00001)
	    IO.output(TRIG_FRONT, False)

	    while IO.input(ECHO_FRONT)==0:
	      pulse_start = time.time()

	    while IO.input(ECHO_FRONT)==1:
	      pulse_end = time.time()

	    pulse_duration = pulse_end - pulse_start
	    distance = pulse_duration * 17150
	    distance_frontside = round(distance, 2)

	    #print ("Distance:",distance,"cm")
            return distance_frontside

def backSensor():


	    IO.output(TRIG_BACK, False)
	    time.sleep(0.1)
	    IO.output(TRIG_BACK, True)
	    time.sleep(0.00001)
	    IO.output(TRIG_BACK, False)

	    while IO.input(ECHO_BACK)==0:
	      pulse_start = time.time()

	    while IO.input(ECHO_BACK)==1:
	      pulse_end = time.time()

	    pulse_duration = pulse_end - pulse_start
	    distance = pulse_duration * 17150
	    distance_backside = round(distance, 2)

	    #print ("Distance:",distance,"cm")
            return distance_backside

def front_avoidence():
    print("STOP")
    allStop()
    time.sleep(1)
    print("SPINNING")
    reverseDrive()
    time.sleep(0.6)
    SpinRight()
    time.sleep(0.6)

def back_avoidence(distance_frontside):
    if distance_frontside>20:
    	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 1
	driveRight.value = 1
	time.sleep(0.5)
	print("AVOID BACKSIDE HIT")
    else :
        print("EMERGENCY BREAK")
        allStop()
        time.sleep(3)




def main():


	#distance_backside=backSensor()
	distance_frontside=frontSensor()
	distance_backside=backSensor()
        print(distance_frontside)
        if distance_frontside<15:
            front_avoidence()
        if distance_backside<10:
            back_avoidence(distance_frontside)
        elif(IO.input(LEFT_IR)==True and IO.input(RIGHT_IR)==True): #both white move forward
            allStop()
            print("stop")
	elif(IO.input(LEFT_IR)==False and IO.input(RIGHT_IR)==True): #turn right
            forwardTurnRight()
            print("right turn")
        elif(IO.input(LEFT_IR)==True and IO.input(RIGHT_IR)==False): #turn left
            forwardTurnLeft()
            print("left turn")
        else:
            forwardDrive()
            print("forward move")

while 1:

        main()
