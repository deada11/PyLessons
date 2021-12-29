import csv
from collections import Counter

crimes = []
with open("Crimes.csv") as file:
    reader = csv.DictReader(file, delimiter=',')
    for obj in reader:
        crimes.append(obj['Primary Type'])  # Обращение по ключу 'Primary Type' к объекту reader
    b = Counter(crimes).most_common(1)
    print(b)
