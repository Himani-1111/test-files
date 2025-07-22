# Import motor control classes for X, Y, and Z axes
from motors.motor_x import MotorX
from motors.motor_y import MotorY
from motors.motor_z import MotorZ

# Import endstop classes for X, Y, and Z axes
from endstops.endstop_x import EndstopX
from endstops.endstop_y import EndstopY
from endstops.endstop_z import EndstopZ

class MotionController:
    def __init__(self, gpio):
        # Initialize motor objects for each axis, passing GPIO interface
        self.motor_x = MotorX(gpio)
        self.motor_y = MotorY(gpio)
        self.motor_z = MotorZ(gpio)
        # Initialize endstop objects for each axis, passing GPIO interface
        self.endstop_x = EndstopX(gpio)
        self.endstop_y = EndstopY(gpio)
        self.endstop_z = EndstopZ(gpio)

    def home_all_axes(self):
        # Move all axes to their home position using endstops
        self.motor_x.home(self.endstop_x)
        self.motor_y.home(self.endstop_y)
        self.motor_z.home(self.endstop_z)

    def move_to(self, x=None, y=None, z=None, feedrate=1000):
        # Move X, Y, and Z motors to the specified positions (in mm)
        if x is not None:
            self.motor_x.move_mm(x)
        if y is not None:
            self.motor_y.move_mm(y)
        if z is not None:
            self.motor_z.move_mm(z)

    def execute_gcode(self, cmd):
        # Execute a G-code command dictionary
        if cmd['command'] in ['G0', 'G1']:  # Linear or rapid move
            self.move_to(x=cmd.get('X'), y=cmd.get('Y'), z=cmd.get('Z'), feedrate=cmd.get('F', 1000))
        elif cmd['command'] == 'G28':       # Home all axes
            self.home_all_axes()

    def print_step_status(self):
        # Print the total steps taken by each motor
        print(f"X: {self.motor_x.total_steps} steps, Y: {self.motor_y.total_steps} steps, Z: {self.motor_z.total_steps} steps")
