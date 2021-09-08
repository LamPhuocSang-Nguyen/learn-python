from math import sqrt
n = int(input('Enter n = '))
s = 0
for i in range(1, n + 1):
    s = sqrt(i + s)
print('S = ', s)