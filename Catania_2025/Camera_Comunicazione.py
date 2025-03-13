from picamera2 import Picamera2
from time import sleep
import numpy as np 
import cv2 

path = '/home/pi/Desktop/Raspberry/Catania_2025/image.jpg'  # Percorso in cui salvare la foto

color = "Undefined"
a = 1

camera = Picamera2()
camera_config = camera.create_still_configuration({"size": (1920, 1080)})  # Risoluzionw 1920x1080
camera.configure(camera_config)

def elabora_immagine(img1):
   
   global color  # Aggiunto per aggiornare la variabile globale color
   img = cv2.convertScaleAbs(img1, 1, 1) 
   hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   height, width, _ = img.shape

   # Coordinate del centro
   cx = int(width / 2)
   cy = int(height / 2)

   # Definire una regione 100x100 attorno al centro
   roi_size = 50  # Metà dimensione della ROI
   roi = hsv_frame[cy - roi_size:cy + roi_size, cx - roi_size:cx + roi_size]

   # Calcolare il colore medio nella ROI
   mean_color = cv2.mean(roi)[:3]  # Ignorare il canale alpha
   hue_value = int(mean_color[0])
   sat_value = int(mean_color[1])
   value_value = int(mean_color[2])

   # Determinare il colore predominante
   if value_value < 50:
      color = b"BLACK"
   elif sat_value < 50:
      color = b"WHITE"
   else:
      if hue_value < 5:
         color = b"RED"
      elif hue_value < 22:
         color = b"ORANGE"
      elif hue_value < 33:
         color = b"YELLOW"
      elif hue_value < 78:
         color = b"GREEN"
      elif hue_value < 131:
         color = b"BLUE"
      elif hue_value < 167:
         color = b"VIOLET"
      else:
         color = b"RED"

import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

def send(value):
   """Invia un messaggio e aspetta conferma 'ok' da Arduino."""
   while True:
      ser.write(value)
      line = ser.readline().decode('utf-8').rstrip()
      if line == "ok":
         break

def receive():
   
   """Riceve un messaggio da Arduino e risponde con 'ok'."""
   while True:
      line = ser.readline().decode('utf-8').rstrip()
      if line:  # Controlla se la stringa non è vuota
         ser.write(b"ok\n")  # Conferma la ricezione
         return line
      
while True:
   
   if receive() == "rileva":
      
      camera.start()             # Avvia la fotocamera
      sleep(1)                   # Attendi che la fotocamera si avvii
      camera.capture_file(path)  # Salva l'immagine nella cartella
      camera.stop()              # Arresta la fotocamera
      
      img1 = cv2.imread(path)    # Leggi l'immagine salvata

      elabora_immagine(img1)     # Ricava colore
      print(color)
      
      send(color)
      
   sleep(0.1)