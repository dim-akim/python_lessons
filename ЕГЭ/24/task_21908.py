import re


with open('24_21908.txt') as file:
    text = file.readline()

pattern = r'[1-9A-D][0-9A-D]+'

result = re.findall(pattern, text)

print(result)
print(max(result, key=len))
