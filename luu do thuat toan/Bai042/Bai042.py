n = eval(input('Enter n = '))
S = 0
i = 1
while (i <= n):
    S = S + (1 / (i * (i + 1)))
    i = i + 1

print('S =', S)
