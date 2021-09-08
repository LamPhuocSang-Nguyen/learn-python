from math import sqrt
n = int(input('Enter n = '))
s = 0
for i in range(n):
    s = sqrt(2 + s)
print('S = ', s)