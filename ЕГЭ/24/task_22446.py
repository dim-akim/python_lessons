with open('24_22446.txt') as file:
    text = file.readline()

left = max_len = count_lnd = 0
start = left + 1

while count_lnd < 10000:
    if text[start - 2:start + 1] == 'LND':
        count_lnd += 1
    start += 1
print(f'{start=}')
for right in range(start, len(text)):
    if text[right - 2:right + 1] == 'LND':
        count_lnd += 1

    while count_lnd > 10000:
        if text[left:left + 3] == 'LND':
            count_lnd -= 1
        left += 1
        print(f'{left=}')

    for l1 in range(left, right):
        if text[l1] == text[right]:
            length = right - l1 + 1
            if length > max_len:
                max_len = length
                print(f'{length=} {l1=} {right=}')
print(max_len)
