import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

liga = 1
desliga = 0
tempo = 5

def acendeled(pino_led):
	GPIO.setup(pino_led,GPIO.OUT)
	GPIO.output(pino_led,GPIO.HIGH)
	
def apagaled(pino_led):
	GPIO.setup(pino_led,GPIO.OUT)
	GPIO.output(pino_led,GPIO.LOW)
'''
while tempo > 0:
    acendeled(18)
    print('on')
    time.sleep(2)
    apagaled(18)
    time.sleep(2)
    print('off')
    tempo -= 1
    '''