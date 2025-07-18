from libraries import gpio_interface
from motion_control import MotionController
from gcode_parser import GCodeParser

def main():
    gpio = gpio_interface()
    motion = MotionController(gpio)
    parser = GCodeParser()
    
    with open('input.gcode', 'r') as f:
        gcode_lines = f.readlines()

    motion.home_all_axes()

    for line in gcode_lines:
        cmd = parser.parse_line(line)
        if cmd:
            motion.execute_gcode(cmd)
            motion.print_step_status()

if __name__ == "__main__":
    main()