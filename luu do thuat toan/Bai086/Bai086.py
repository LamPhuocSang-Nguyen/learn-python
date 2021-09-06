x = eval(input('Enter x = '))
n = int(input('Enter n = '))
s = 0
T = 1
sign = -1
for i in range(0, 2 * n, 2):
    T = T * x * x
    s = s + sign * T
    sign = -sign
print('S = ', s)