from libraries import gpio_interface         # Import GPIO interface library for hardware interaction
from motion_control import MotionController  # Import the MotionController class to manage movements
from gcode_parser import GCodeParser         # Import GCodeParser for interpreting G-code instructions

def main():
    gpio = gpio_interface()                 # Initialize GPIO interface (hardware pins, etc.)
    motion = MotionController(gpio)         # Create a MotionController using the GPIO interface
    parser = GCodeParser()                  # Create a GCodeParser instance for parsing G-code

    # Read all lines from the G-code input file
    with open('input.gcode', 'r') as f:
        gcode_lines = f.readlines()

    motion.home_all_axes()                  # Move all axes to their home positions before starting

    # Process each line of G-code from the input file
    for line in gcode_lines:
        cmd = parser.parse_line(line)       # Parse the G-code line to a command
        if cmd:
            motion.execute_gcode(cmd)       # Execute the parsed G-code command
            motion.print_step_status()      # Print the current status after executing the step

if __name__ == "__main__":
    main()                                  # Run the main function if this script is executed
