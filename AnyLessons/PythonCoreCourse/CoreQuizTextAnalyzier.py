def count_char(words, character):
    count = 0
    for c in words:
        if c == character:
            count += 1
    return count


filename = input("Enter a filename: ")

with open(filename) as f:
    text = f.read()


for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print(f"{char} - {round(perc, 2)}%")
