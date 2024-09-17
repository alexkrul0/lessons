from random import randint

n = randint(3, 20)
result = []
pares = []

for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result.extend([i, j])
            # result += str(i) + str(j)
            # result += f'{i}{j}'
        pares.append([i, j])

result = list(map(str, result))
result = ''.join(result)
print(n)
print(result)
print(pares)
