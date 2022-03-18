max_cnt = 0
with open('inf_26_04_21_24.txt') as file:
    for line in file:
        if line.count('G') < 25:
            for letter in line:
                cnt = line.rfind(letter) - line.find(letter)
                max_cnt = max(cnt, max_cnt)
print(max_cnt)


number = 6 * 512**180 + 7 * 64**181 + 3 * 8**184 + 5 * 8**125 - 65
cnt = 0
while number > 0:
    if number % 64 == 0:
        cnt += 1
    number //= 64
print(cnt)
