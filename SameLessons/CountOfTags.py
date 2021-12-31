import re
from urllib.request import urlopen
from collections import Counter


regex = '<code>(.*?)</code>'
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s = str(html)
unsorted_list = sorted(re.findall(regex, s))
sorted_list = Counter(unsorted_list)
sorted_list.most_common()

print(sorted_list)
