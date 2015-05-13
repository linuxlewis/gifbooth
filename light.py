import time
from time import sleep
import RPi.GPIO as GPIO


class LightManager:

    def __init__(self, pins=()):
        self.lights = []

        for pin in pins:
            self.lights.append(Light(pin))

    def add_light(self, pin_number):
        self.lights.append(Light(pin_number))

    def flash(self, seconds=3):
        stop_at = time.time() + seconds
        while time.time() < stop_at:
            list(map(lambda x: x.turn_light_on(), self.lights))
            sleep(0.2)
            list(map(lambda x: x.turn_light_off(), self.lights))
            sleep(0.2)
        map(lambda x: x.turn_light_off(), self.lights)

    def final_countdown(self):
        """
        blink the lights over 3 seconds to countdown
        """
        for light in self.lights:
            light.turn_light_on()
            sleep(1)
            light.turn_light_off()
        self.flash()


class Light:

    def __init__(self, pin_number):
        self.pin_number = pin_number
        GPIO.setup(self.pin_number, GPIO.OUT)

    def turn_light_on(self):
        GPIO.output(self.pin_number, True)

    def turn_light_off(self):
        GPIO.output(self.pin_number, False)
