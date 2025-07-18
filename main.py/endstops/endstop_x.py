class EndstopX:
    def __init__(self, gpio):
        self.gpio = gpio
        self.pin = 59 # Pin number 19 for Endstop X 
        self.gpio.setup(self.pin, self.gpio.IN, pull_up_down=self.gpio.PUD_UP)

    def is_not_triggered(self):
        return self.gpio.input(self.pin)