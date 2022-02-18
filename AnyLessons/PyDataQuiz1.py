string = input()
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0
for letter in string:
    if letter in vowels:
        count += 1
print(count)
