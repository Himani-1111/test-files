# GCode Motion Controller

This repository implements a Python-based GCode motion control system, suitable for controlling a 3-axis CNC or 3D printer using GPIO (such as on an Axon). The project parses GCode files and translates movement commands into motor operations, with support for endstop homing and step status reporting.

---

## Features

- **GCode Parsing:** Reads and interprets `.gcode` files, supporting standard movement and homing commands.
- **Motor Control:** Drives X, Y, and Z stepper motors via GPIO pins.
- **Endstop Support:** Homes each axis using endstop switches for precise zeroing.
- **Step Reporting:** Prints total steps moved for each axis after every command.

## Directory Structure

```
main.py/
├── main.py             # Entry point; orchestrates parsing and motion
├── gcode_parser.py     # GCode parsing logic
├── motion_control.py   # High-level motion control and homing
├── libraries.py        # GPIO library abstraction
├── motors/
│   ├── motor_x.py      # MotorX class (X axis)
│   ├── motor_y.py      # MotorY class (Y axis)
│   └── motor_z.py      # MotorZ class (Z axis)
├── endstops/
│   ├── endstop_x.py    # EndstopX class (X axis endstop)
│   ├── endstop_y.py    # EndstopY class (Y axis endstop)
│   └── endstop_z.py    # EndstopZ class (Z axis endstop)
```

## Usage

1. Place a GCode file named `input.gcode` in the project directory.
2. Run the main script:
   ```bash
   python main.py/main.py
   ```
3. The system will home all axes, then execute movement commands from the GCode file.

## Requirements

- Python 3.x
- Axon by Vicharak (or compnatible GPIO hardware)
- Libraries:  `axon_gpio` (automatically detected)

## How It Works

- **Initialization:** The main script sets up GPIO, motors, and endstops.
- **Homing:** All axes are homed using endstops for reference.
- **Execution:** Each line of GCode is parsed and, if valid, triggers corresponding motor movements.

## Code Overview

- `main.py`: Loads the GCode file, initializes objects, and manages the control loop.
- `gcode_parser.py`: Extracts commands and parameters from GCode lines.
- `motion_control.py`: Coordinates motor movements and homing routines.
- `motors/`: Contains axis-specific motor classes for step/dir/en signals.
- `endstops/`: Contains endstop classes for each axis.

