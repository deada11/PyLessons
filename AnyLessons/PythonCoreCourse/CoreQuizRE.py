import re

number = input()
pattern = r'^[1|8|9][\d]{7}$'

if re.match(pattern, number):
    print("Valid")
else:
    print("Invalid")
