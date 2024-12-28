#!/usr/bin/python

pin = 1

#LIBRERIE

import RPi.GPIO as GPIO       #libreria per utilizzare pin di raspberry
import gpiozero               #contiene funzioni già scritte pr componenti base
import time                   #permette di gestire tempo

#COMANDI "setup"

GPIO.setmode(GPIO.BOARD)      #con questa impostazione il numero dei pin corrisponde alla posizione fisica che hanno (alternativa a GPIO.BCM)
GPIO.setmode(GPIO.BCM)        #con questa impostazione il numero dei pin corrisponde a questa mappa: https://raspi.tv/wp-content/uploads/2013/07/Rev2-GPIO-bold.jpg

GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT / GPIO.IN)       #dichiari pin come output o input

#COMANDI "loop"

GPIO.output(pin, GPIO.HIGH / GPIO.LOW)    #assegna valore alto o basso al pin
GPIO.input(pin)                           #leggi valore del pin

time.sleep(1)                             #delay in secondi