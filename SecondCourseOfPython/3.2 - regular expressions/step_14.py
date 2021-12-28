import re
import sys
incoming_pattern = r'\b(\w)(\w)'
# outcoming_pattern = r'\2\1' закомментировал, т.к. сырую строку с шаблоном можно использовать в sub()
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(incoming_pattern, r'\2\1', line))
