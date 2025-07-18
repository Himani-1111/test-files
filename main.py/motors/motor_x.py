import time

class MotorX:
    def __init__(self, gpio, step_pin=14, dir_pin=13, en_pin=16, steps_per_mm=200 * 256 / 8):
        """
        Initialize the MotorX class.

        :param gpio: GPIO interface object
        :param step_pin: GPIO pin for step signal
        :param dir_pin: GPIO pin for direction signal
        :param en_pin: GPIO pin for enable signal
        :param steps_per_mm: Steps required to move 1 mm
        """
        self.gpio = gpio
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.en_pin = en_pin
        self.steps_per_mm = steps_per_mm
        self.total_steps = 0

        # Setup GPIO pins step=2, dir=4, and enable=13
        self.gpio.setup(self.step_pin, self.gpio.OUT)
        self.gpio.setup(self.dir_pin, self.gpio.OUT)
        self.gpio.setup(self.en_pin, self.gpio.OUT)
        self.disable_motor()

    def enable_motor(self):
        """Enable the motor by setting the enable pin to LOW."""
        self.gpio.output(self.en_pin, 0)

    def disable_motor(self):
        """Disable the motor by setting the enable pin to HIGH."""
        self.gpio.output(self.en_pin, 1)

    def home(self, endstop, home_dir=0):
        """
        Home the motor until the endstop is triggered.

        :param endstop: Endstop object with an `is_not_triggered` method
        :param home_dir: Direction to move for homing (0 or 1)
        """
        if not hasattr(endstop, 'is_not_triggered'):
            raise ValueError("Endstop object must have an 'is_not_triggered' method.")

        self.enable_motor()
        self.gpio.output(self.dir_pin, home_dir)
        while endstop.is_not_triggered():
            self._step_once()

        # Move a few steps away from the endstop
        self.gpio.output(self.dir_pin, 1 - home_dir)
        for _ in range(10):
            self._step_once()
        self.disable_motor()

    def move_mm(self, mm, direction=1):
        """
        Move the motor a specified distance in mm.

        :param mm: Distance to move in mm
        :param direction: Direction to move (0 or 1)
        """
        steps = int(mm * self.steps_per_mm)
        self.enable_motor()
        self.gpio.output(self.dir_pin, direction)
        for _ in range(steps):
            self._step_once()
        self.disable_motor()

    def _step_once(self):
        """Perform a single step."""
        self.gpio.output(self.step_pin, 1)
        time.sleep(0.0005)
        self.gpio.output(self.step_pin, 0)
        time.sleep(0.0005)
        self.total_steps += 1