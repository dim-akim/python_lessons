from urllib.request import urlopen
html: str = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
state = 0
i = 0
result = []
s = ''

while i < len(html)-7:
    if html[i:i+6] == '<code>':
        state = 1
        i += 6
    elif html[i:i+7] == '</code>':
        state = 0
        i += 7
        result.append(s)
        s = ''
    elif state == 1:
        s += html[i]
        i += 1
    else:
        i += 1

d = {}
for item in result:
    d[item] = result.count(item)

for key in sorted(d, key=lambda x: d[x], reverse=True):
    print(d[key], key)
