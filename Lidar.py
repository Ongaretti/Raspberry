import RPi.GPIO as GPIO       #libreria per utilizzare pin di raspberry
import time

def pulse_in(pin, level, timeout):
    
   start_time = time.time()
   # Aspetta che il pin cambi allo stato desiderato
   while GPIO.input(pin) != level:
      if time.time() - start_time > timeout:
         return 0
      
   # Registra il tempo di inizio dell'impulso
   start_time = time.time()
   # Aspetta che il pin cambi dallo stato desiderato
   while GPIO.input(pin) == level:
      if time.time() - start_time > timeout:
         return 0
      end_time = time.time()

   # Calcola la durata dell'impulso
   pulse_duration = end_time - start_time

   return pulse_duration
   

# Esempio di utilizzo
pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN)

while True:
   tempo = pulse_in(pin, GPIO.HIGH, 1.85)
   print(tempo*1000)
   
   distanza = (tempo*1000) *3/4

   if distanza < 0:
      distanza = 0

   #print(distanza)

   time.sleep(0.2)