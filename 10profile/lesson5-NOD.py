a = 10
b = 4

if a < b:
    nod = a
else:
    nod = b

while nod > 1:
    if a % nod == 0 and b % nod == 0:
        print(nod)
        break
    nod = nod - 1
