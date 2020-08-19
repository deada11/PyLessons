d = int(input())
words = [input().lower() for i in range(d)]
l = int(input())
templateText = [input().lower() for j in range(l)]
text = []
errors = []
for i in range(0, l):
    text.extend(templateText[i].split(' '))

for i in text:
    if i not in words and i not in errors:
        errors.append(i)

print('\n'.join(errors))