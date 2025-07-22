import re

class GCodeParser:
    # Parses a single line of G-code and extracts command and parameters
    def parse_line(self, line):
        line = line.strip()  # Remove leading/trailing whitespace
        if not line or line.startswith(';'):  # Ignore empty lines or comments
            return None
        # Match lines starting with 'G', 'M', or 'T' followed by numbers
        match = re.match(r'([GMT]\d+)\s*(.*)', line)
        if not match:  # If line doesn't match expected format, skip
            return None
        command = match.group(1)  # Extract command (e.g., G1, M3)
        params = match.group(2)   # Extract remainder (parameters)
        result = {'command': command}  # Initialize result dictionary
        # Split parameters and process each one
        for p in params.split():
            if p[0] in "XYZF":  # Only interested in X, Y, Z, F parameters
                try:
                    result[p[0]] = float(p[1:])  # Convert parameter value to float
                except ValueError:
                    pass  # Ignore parameters that can't be converted
        return result  # Return parsed command and parameters
