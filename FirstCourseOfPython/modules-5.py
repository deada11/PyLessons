import requests
count = 0
domain = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('dataset_3378_3.txt') as first:
    url1 = first.read().strip()
urlOld = requests.get(url1).text
while True:
    urlNew = domain + requests.get(domain + urlOld).text
    count += 1
    if urlNew.endswith('.txt') == False:
        break
    urlOld = requests.get(urlNew).text
    print(urlNew, urlOld, count)

print(requests.get(domain + urlOld).text)