from picamera2 import Picamera2
from time import sleep
import numpy as np 
import cv2 

# Inizializza la fotocamera (config per streaming video)
camera = Picamera2()
camera_config = camera.create_video_configuration(main={"size": (640, 480)})  # risoluzione ridotta per realtime
camera.configure(camera_config)
camera.start()
sleep(0.1)  # lascia stabilizzare la camera

# Mostra il feed in una finestra OpenCV
try:

    while True:
        frame = camera.capture_array()  # NumPy array in RGB

        height, width, _ = frame.shape
        x = int(width / 2)
        y = int(height / 2)

        # Converti in HSV (da RGB), costruisci maschera per il rosso
        hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

        roi = hsv[y - 25:y + 25, x - 25:x + 25]
        mean_color = cv2.mean(roi)[:3]

        hue_value = int(mean_color[0])
        sat_value = int(mean_color[1])
        value_value = int(mean_color[2])

        if hue_value < 10 or hue_value > 135:
            color = "RED"
        elif hue_value < 58:
            color = "YELLOW"
        elif hue_value < 93:
            color = "GREEN"
        elif hue_value < 135:
            color = "BLUE"

        print(color, "\t", hue_value, sat_value, value_value)

        # Converti l'immagine in BGR per disegnare e mostrare con OpenCV
        img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
        cv2.rectangle(img, (x, y), (x + 50, y + 50), (0, 255, 0), 2)

        cv2.imshow("PiCamera Preview", img)

        sleep(0.1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass

finally:
    # Chiudi tutto
    cv2.destroyAllWindows()
    camera.stop()