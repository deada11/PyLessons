txt = 'one test vulnerable pester awesome'

longest = ''
for word in txt.split(" "):
    if len(word) > len(longest):
        longest = word

print(longest)
