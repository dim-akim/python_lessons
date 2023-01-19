file = open('24_2.txt')
s = file.readline()
count = maxx = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count = count + 1
    else:
        if maxx < count:
            maxx = count
        count = 0
if maxx < count:
    maxx = count
print(maxx + 1)
file.close()
