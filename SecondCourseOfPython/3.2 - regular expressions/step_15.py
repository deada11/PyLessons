import re
import sys

incoming_pattern = r'(\w)\1+'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(incoming_pattern, r'\1', line))
