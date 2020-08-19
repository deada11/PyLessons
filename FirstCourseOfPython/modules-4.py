import requests

with open('dataset_3378_2.txt') as example:
    url = example.read().strip()

resp = requests.get(url).text
strings = resp.splitlines()

print(len(strings), type(strings))