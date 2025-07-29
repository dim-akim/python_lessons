with open('24_22448.txt') as file:
    text = file.readline()

max_len = 0
left = 1
right = 2
is_odd = True
last_word = last_number = ''

while right < len(text):
    last, current = text[right-1:right+1]
    if current.isdigit():
        last_number += current
        if last.isalpha():
            if right - left > max_len:
                max_len = right - left
                print(f'{max_len=} {text[left:right]}')
            last_number = current

    elif current.isalpha():
        if last.isdigit():
            digit = int(last)
            if digit % 2 != is_odd:
                length = right - len(last_number) - left
                if length > max_len:
                    max_len = length
                    print(f'{max_len} {text[left:left+length]}')
                is_odd = digit % 2
                left = right - len(last_number) - len(last_word) + 1
            last_word = current
        last_word += current

    right += 1
