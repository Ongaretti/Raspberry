import RPi.GPIO as GPIO

pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin,GPIO.OUT)
print("funziona!")
GPIO.output(pin,GPIO.HIGH)


