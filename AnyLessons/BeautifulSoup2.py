from urllib.request import urlopen
from bs4 import BeautifulSoup

summa = 0
html = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html').read().decode('UTF-8')
s = str(html)
soup = BeautifulSoup(s, 'html.parser')
for tag in soup.find_all('td'):
    summa += int(tag.string)
print(summa)
