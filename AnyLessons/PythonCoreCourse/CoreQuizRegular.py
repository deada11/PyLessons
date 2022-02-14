import re
text = input()

pattern = r'#\w+'
hastags = re.findall(pattern, text)

for hastag in hastags:
    print(hastag)
