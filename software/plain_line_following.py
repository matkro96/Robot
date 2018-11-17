import RPi.GPIO as IO
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep
from __future__ import division


#//////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////SET MOTOR SPEED//////////////////////////////////////
#/////////////////////////// RANGE:  0...100[%}////////////////////////////////////
forward_speed=50#[%]
reverse_speed=100#[%]
turns_speed=100#[%]
#///////////////////////////////////////////////////////////////////////////////////

LEFT_IR=14
RIGHT_IR=3

PWM_DRIVE_LEFT = 21		# ENA - H-Bridge enable pin
FORWARD_LEFT_PIN = 26	# IN1 - Forward Drive
REVERSE_LEFT_PIN = 19	# IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_DRIVE_RIGHT = 5		# ENB - H-Bridge enable pin
FORWARD_RIGHT_PIN = 13	# IN1 - Forward Drive
REVERSE_RIGHT_PIN = 6	# IN2 - Reverse Drive

IO.setup(LEFT_IR,IO.IN) #GPIO 2 -> Left IR out
IO.setup(RIGHT_IR,IO.IN) #GPIO 3 -> Right IR out

# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)

# Initialise objects for H-Bridge digital GPIO pins
forwardLeft = DigitalOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = DigitalOutputDevice(REVERSE_LEFT_PIN)
forwardRight = DigitalOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = DigitalOutputDevice(REVERSE_RIGHT_PIN)

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
	driveLeft.value = (forward_speed/100
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
	driveLeft.value = turns_speed/400
	driveRight.value = turns_speed/100

def forwardTurnRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = turns_speed/100
	driveRight.value = turns_speed/400

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

def main():
        if(IO.input(LEFT_IR)==True and IO.input(RIGHT_IR)==True): #both white move forward
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
            print(round(50/100, 2))
            print("forward move")

while 1:

        main()
