import re

class GCodeParser:
    def parse_line(self, line):
        line = line.strip()
        if not line or line.startswith(';'):
            return None
        match = re.match(r'([GMT]\d+)\s*(.*)', line)
        if not match:
            return None
        command = match.group(1)
        params = match.group(2)
        result = {'command': command}
        for p in params.split():
            if p[0] in "XYZF":
                try:
                    result[p[0]] = float(p[1:])
                except ValueError:
                    pass
        return result