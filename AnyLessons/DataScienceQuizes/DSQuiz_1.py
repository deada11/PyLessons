import math

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
mean = 0
for i in players:
    mean += i

mean /= len(players)

variance = 0
for j in players:
    k = (j - mean)**2
    variance += k
variance /= len(players)

standard_deviation = math.sqrt(variance)
print(f"Mean = {mean}")
print(f"Variance = {variance}")
print(f"Standard_deviation = {standard_deviation}")
print(mean - standard_deviation, mean + standard_deviation)
count = 0
for height in players:
    if (mean - standard_deviation) < height < (mean + standard_deviation):
        count += 1

print(count)
