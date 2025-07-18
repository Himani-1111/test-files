try:
    import axon_gpio as GPIO
except ImportError:
    import RPi.GPIO as GPIO

def gpio_interface():
    GPIO.setmode(GPIO.BCM)
    return GPIO