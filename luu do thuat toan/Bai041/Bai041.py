n = eval(input('Enter n = '))
S = 0
i = 1
while (i <= n):
    S = S + i * (i + 1) * (i + 2)
    i = i + 1

print('S =', S)
