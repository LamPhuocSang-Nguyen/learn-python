from math import sin
x = eval(input('Enter x = '))
n = int(input('Enter n = '))
s = 0
T = x
for i in range(1, n + 1):
    T = sin(T)
    s = s + T
print('S = ', s)