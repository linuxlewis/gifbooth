import time
from time import sleep
import RPi.GPIO as GPIO


def turn_light_on(pin_number):
    if isinstance(pin_number, list):
        for pin in pin_number:
            GPIO.output(pin, True)
    else:
        GPIO.output(pin_number, True)


def turn_light_off(pin_number):
    if isinstance(pin_number, list):
        for pin in pin_number:
            GPIO.output(pin, False)
    else:
        GPIO.output(pin_number, False)


def flash(seconds=3):
    stop_at = time.time() + seconds
    while time.time() < stop_at:
        turn_light_on([23, 27, 22])
        sleep(0.2)
        turn_light_off([23, 27, 22])
        sleep(0.2)
    turn_light_off([23, 27, 22])


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    while True:
        value = GPIO.input(17)
        if value:
            turn_light_on(23)
            sleep(1)
            turn_light_off(23)
            turn_light_on(27)
            sleep(1)
            turn_light_off(27)
            turn_light_on(22)
            sleep(1)
            flash()
            while value:
                value = GPIO.input(17)
