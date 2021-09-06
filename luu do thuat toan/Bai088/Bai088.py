n = int(input('Enter n = '))
s = 0
M = 0
sign = 1
for i in range(1, n + 1):
    M = M + i
    s = s + sign * (1 / M)
    sign = -sign
print('S = ', s)