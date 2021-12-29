import requests

params = {
    'json': 'true'
}
answer = []
with open('dataset_24476_3.txt') as file:
    prev_integers = file.readlines()
    integers = [i.rstrip() for i in prev_integers]

for i in integers:
    url = f'http://numbersapi.com/{i}/math'
    res = requests.get(url, params=params)
    data = res.json()
    if data['found'] is True:
        answer.append('Interesting')
    else:
        answer.append('Boring')

with open('out.txt', 'w') as output:
    for line in answer:
        output.write(line + '\n')

#  Надо интереса для переписать с учетом того, что цифры можно передавать в урл в виде списка через запятую.
