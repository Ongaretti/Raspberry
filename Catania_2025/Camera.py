from picamera2 import Picamera2
from time import sleep
import numpy as np 
import cv2 

color = "Undefined"
a=1

def elabora_immagine():
   
   img = cv2.convertScaleAbs(img1, 1, 1) 
   hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   height, width, _ = img.shape

   # Center coordinates
   cx = int(width / 2)
   cy = int(height / 2)

   # Define a 100x100 region around the center
   roi_size = 50  # Half-size of the ROI
   roi = hsv_frame[cy - roi_size:cy + roi_size, cx - roi_size:cx + roi_size]

   # Calculate the mean color in the ROI
   mean_color = cv2.mean(roi)[:3]  # Ignore alpha channel
   hue_value = int(mean_color[0])
   sat_value = int(mean_color[1])
   value_value = int(mean_color[2])

   # Determine the predominant color
   color = "Undefined"
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
         color= "YELLOW"
      elif hue_value < 78:
         color = " GREEN"
      elif hue_value < 131:
         color = "BLUE"
      elif hue_value < 167:
         color = "VIOLET"
      else:
         color = "RED"

camera = Picamera2()
camera.resolution = (1920, 1080)

while(a == 1):

   camera.capture('/home/pi/Desktop/image.jpg')
   img1 = cv2.imread('/home/pi/Desktop/image.jpg')
   
   elabora_immagine()
   print(color)
   
   a+=1

   