import re
import sys
incoming_pattern = r'(\b[Aa]+\b)'
outcoming_pattern = 'argh'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(incoming_pattern, outcoming_pattern, line, 1))
