number = 9 * 57**2024 + 14 * 13**3059 - 87 * 67**1111 + 2027
ans = []

while number:
    ans.append(number % 36)
    number //= 36

print(ans)
print(len([i for i in ans if i > 20]))
