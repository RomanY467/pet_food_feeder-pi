from gpiozero import Servo
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(12, min_pulse_width=0.5/1000,
              max_pulse_width=2.5/1000, pin_factory=factory)


def feed():
    for i in range(2):
        print("Go to min")
        servo.min()
        sleep(2)
        print("Go to max")
        servo.max()
        sleep(2)
        print("And back to middle")
        servo.mid()
        sleep(2)
    servo.value = None
