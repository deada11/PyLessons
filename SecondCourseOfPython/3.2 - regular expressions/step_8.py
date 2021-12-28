import re
import sys
pattern = r'(\bcat\b)'  # А если сделать r'(\b[Cc]at\b)', то еще и большие буквы попадут в выборку
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)
