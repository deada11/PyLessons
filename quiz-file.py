file = open('dataset_3363_3.txt', 'r')
data = file.read()
data_copy = list(data.split())
subdata = list(data.lower().split())
counts = []
s_counts = []

for i in range(0, len(subdata)):
    counts.append(subdata.count(subdata[i]))

for k in range(0, len(data_copy)):
    s_counts.append(data_copy.count(data_copy[k]))
#print(data)

#print(type(counts), counts)
#print(type(subdata), subdata)

#print(type(s_counts), s_counts)
#print(type(data_copy), data_copy)

d = dict(zip(subdata, counts))
inv_d = [(value, key) for key, value in d.items()]
end = list(max(inv_d))

print(end)
output = open('output_file.txt', 'w')
for elems in reversed(end):
    output.write(str(elems))
    output.write(' ')
output.close()

