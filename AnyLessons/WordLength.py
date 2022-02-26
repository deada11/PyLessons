text = input()

counter = 0
for i in text.split():
    counter += len(i)

print(counter / len(text.split()))
