n = int(input('Enter n = '))
M = 0
S = 0
for i in range(1, n + 1):
    M = M + i
    S = S + (1 / M)
print('S = ', S)