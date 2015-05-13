import RPi.GPIO as GPIO


class InputButton:

    def __init__(self, pin_number=17):
        GPIO.setmode(GPIO.BCM)
        self.pin_number = pin_number
        GPIO.setup(self.pin_number, GPIO.IN)

    def add_onclick_callback(self, callback):
        GPIO.add_event_detect(self.pin_number, GPIO.RISING, callback=callback)
