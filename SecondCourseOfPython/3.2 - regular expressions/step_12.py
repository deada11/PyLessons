import re
import sys

incoming_pattern = r'(human)'
outcoming_pattern = 'computer'
for line in sys.stdin:
    line = line.strip()
    print(re.sub(incoming_pattern, outcoming_pattern, line))

