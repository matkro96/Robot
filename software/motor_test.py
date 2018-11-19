''' this script allows you to test robot motion. If started the robot will check all possible moves as follow:

	forwardDrive
	allStop
	reverseDrive
	spinLeft
	SpinRight
	forwardTurnLeft
	forwardTurnRight
	reverseTurnLeft
	reverseTurnRight

'''
import RPi.GPIO as IO
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep


IO.setup(2,IO.IN) #GPIO 2 -> Left IR out
IO.setup(3,IO.IN) #GPIO 3 -> Right IR out



PWM_DRIVE_LEFT = 21	
FORWARD_LEFT_PIN = 26	# IN1 - Forward Drive
REVERSE_LEFT_PIN = 19	# IN2 - Reverse Drive

PWM_DRIVE_RIGHT = 5	
FORWARD_RIGHT_PIN = 13	# IN1 - Forward Drive
REVERSE_RIGHT_PIN = 6	# IN2 - Reverse Drive


driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)


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
	driveLeft.value = 1.0
	driveRight.value = 1.0

def reverseDrive():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.0
	driveRight.value = 1.0

def spinLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 1.0
	driveRight.value = 1.0

def SpinRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 1.0
	driveRight.value = 1.0

def forwardTurnLeft():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.2
	driveRight.value = 0.8

def forwardTurnRight():
	forwardLeft.value = True
	reverseLeft.value = False
	forwardRight.value = True
	reverseRight.value = False
	driveLeft.value = 0.8
	driveRight.value = 0.2

def reverseTurnLeft():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.2
	driveRight.value = 0.8

def reverseTurnRight():
	forwardLeft.value = False
	reverseLeft.value = True
	forwardRight.value = False
	reverseRight.value = True
	driveLeft.value = 0.8
	driveRight.value = 0.2

def main():
	allStop()
	forwardDrive()
	sleep(1)
	allStop()
	sleep(1)
	reverseDrive()
	sleep(1)
	spinLeft()
	sleep(1)
	SpinRight()
	sleep(1)
	forwardTurnLeft()
	sleep(1)
	forwardTurnRight()
	sleep(1)
	reverseTurnLeft()
	sleep(1)
	reverseTurnRight()
	sleep(1)
	allStop()


main()
