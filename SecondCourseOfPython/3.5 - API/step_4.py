import requests
import json

client_id = 'a05a5cbe6800aca30677'
client_secret = 'e26434a4e2a296ece1af529fa4dd552d'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}
with open('dataset_24476_4.txt') as file:
    prev_artists = file.readlines()
    integers = [i.rstrip() for i in prev_artists]
artists = []
for i in integers:
    # инициируем запрос с заголовком
    r = requests.get(f"https://api.artsy.net/api/artists/{i}", headers=headers)
    r.encoding = 'utf-8'
    # разбираем ответ сервера
    j = json.loads(r.text)
    artists.append((j['birthday'], j['sortable_name']))

artists.sort()

with open('artists_out.txt', 'w') as output:
    for line in artists:
        output.write(line[1] + '\n')
