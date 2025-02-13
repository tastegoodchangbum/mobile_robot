# motor_controller.py
import RPi.GPIO as GPIO

class MotorController:
    def __init__(self):
        self.__motor_pins = {
            "left_forward": 17,
            "left_backward": 18,
            "right_forward": 22,
            "right_backward": 23,
        }

        GPIO.setmode(GPIO.BCM)
        for pin in self.__motor_pins.values():
            GPIO.setup(pin, GPIO.OUT)

    def move_forward(self):
        GPIO.output(self.__motor_pins["left_forward"], GPIO.HIGH)
        GPIO.output(self.__motor_pins["left_backward"], GPIO.LOW)
        GPIO.output(self.__motor_pins["right_forward"], GPIO.HIGH)
        GPIO.output(self.__motor_pins["right_backward"], GPIO.LOW)

    def turn_left(self):
        GPIO.output(self.__motor_pins["left_forward"], GPIO.LOW)
        GPIO.output(self.__motor_pins["left_backward"], GPIO.HIGH)
        GPIO.output(self.__motor_pins["right_forward"], GPIO.HIGH)
        GPIO.output(self.__motor_pins["right_backward"], GPIO.LOW)

    def stop(self):
        for pin in self.__motor_pins.values():
            GPIO.output(pin, GPIO.LOW)
