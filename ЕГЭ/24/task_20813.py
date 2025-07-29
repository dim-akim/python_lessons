import re

with open('24_20813.txt') as file:
    text = file.readline()

# digit = r'(?:[1-9][0-9]*|0)'
# pattern = fr'(?:{digit}[-*])*{digit}'
# result = re.findall(pattern, text)
#
# print(result)
# answer = max(result, key=len)
# print(f'{len(answer)} {answer=}')

max_length = 0
left = 2

for right in range(left + 1, len(text)):
    if text[right] in '-*':
        if right < len(text) and text[right + 1] not in '-*0':
            continue
        elif right < len(text) - 1 and text[right + 1] == '0' and text[right + 2] in '-*':
            continue
        else:
            length = right - left
            if length > max_length:
                print(f'{length=} {text[left:right]}')
                max_length = length
            left = right + 1
            while text[left] in '-*':
                left += 1
