from math import sin
x = eval(input('Enter x = '))
n = int(input('Enter n = '))
s = 0
T = 1
for i in range(1, n + 1):
    T = T * x
    s = s + sin(T)
print('S = ', s)