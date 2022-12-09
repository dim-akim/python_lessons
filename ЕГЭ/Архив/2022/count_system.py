base = 9
n = 883
result = ''

while n > 0:
    d = n % base

    result += str(d)

    n //= base

print(result[::-1])
