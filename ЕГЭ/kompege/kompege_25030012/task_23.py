def f(n):
    answer = result[n - 2]
    if int(n ** 0.5) == n ** 0.5:
        print(f'{n=}')
        answer += result[int(n ** 0.5)]
    if int(n ** (1/3)) == n ** (1/3):
        answer += result[int(n ** (1/3))]
        print(f'{n=} {answer=}')
    return answer


result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

for i in range(11, 1001):
    # print(f'{i=} {f(i)=}')
    result.append(f(i))


print(result[10])
print(result[100])
print(result[1000])
