from picamera2 import Picamera2
import time

camera = Picamera2()
camera_config = camera.create_still_configuration({"size": (640, 480)})
camera.configure(camera_config)
camera.start()
time.sleep(2)  # Attendi che la fotocamera si avvii
camera.capture_file('/home/pi/Desktop/test_image.jpg')
camera.stop()
print("Immagine catturata e salvata come /home/pi/Desktop/test_image.jpg")