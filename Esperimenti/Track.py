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

# HSV bounds per un oggetto rosso (due intervalli per coprire il wrap-around)
lower1 = np.array([0, 120, 70])
upper1 = np.array([10, 255, 255])
lower2 = np.array([135, 120, 70])
upper2 = np.array([255, 255, 255])

# Mostra il feed in una finestra OpenCV
try:
    while True:
        frame = camera.capture_array()  # NumPy array in RGB

        # Converti in HSV (da RGB), costruisci maschera per il rosso
        hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        mask1 = cv2.inRange(hsv, lower1, upper1)
        mask2 = cv2.inRange(hsv, lower2, upper2)
        mask = cv2.bitwise_or(mask1, mask2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))

        cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Converti l'immagine in BGR per disegnare e mostrare con OpenCV
        img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if cnts:
            c = max(cnts, key=cv2.contourArea)
            if cv2.contourArea(c) > 500:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("PiCamera Preview", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass
finally:
    # Chiudi tutto
    cv2.destroyAllWindows()
    camera.stop()