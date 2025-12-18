import RPi.GPIO as GPIO       #libreria per utilizzare pin di raspberry
import gpiozero               #contiene funzioni già scritte pr componenti base
from time import sleep

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

while(True):

   print("ciao")
   GPIO.output(pin, GPIO.HIGH)
   sleep(1)
   GPIO.output(pin, GPIO.LOW)
   sleep(1)