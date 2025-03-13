from picamera2 import Picamera2
from time import sleep
import numpy as np 
import cv2 

color = "Undefined"
a = 1

camera = Picamera2()
camera_config = camera.create_still_configuration({"size": (640, 480)})
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
      color = "BLACK"
   elif sat_value < 50:
      color = "WHITE"
   else:
      if hue_value < 5:
         color = "RED"
      elif hue_value < 22:
         color = "ORANGE"
      elif hue_value < 33:
         color = "YELLOW"
      elif hue_value < 78:
         color = "GREEN"
      elif hue_value < 131:
         color = "BLUE"
      elif hue_value < 167:
         color = "VIOLET"
      else:
         color = "RED"

while a == 1:
   
   camera.start()
   sleep(2)  # Attendi che la fotocamera si avvii
   camera.capture_file('/home/pi/Desktop/Raspberry/Catania_2025/image.jpg')
   camera.stop()
   
   img1 = cv2.imread('/home/pi/Desktop/Raspberry/Catania_2025/image.jpg')

   elabora_immagine(img1)
   print(color)

   a += 1
   
   sleep(1)  # Aggiunto per evitare un ciclo infinito troppo veloce

