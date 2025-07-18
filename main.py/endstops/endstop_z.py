class EndstopZ:
    def __init__(self, gpio):
        self.gpio = gpio
        self.pin = 81 # Pin number 9 for Endstop X 
        self.gpio.setup(self.pin, self.gpio.IN, pull_up_down=self.gpio.PUD_UP)

    def is_not_triggered(self):
        return self.gpio.input(self.pin)