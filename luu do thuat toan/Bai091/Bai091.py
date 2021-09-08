x = eval(input('Enter x = '))
n = int(input('Enter n = '))
s = -1
T = 1
M = 1
sign = 1
for i in range(2, 2 * n + 1, 2):
    T = T * x * x
    M = M * (i - 1) * i
    s = s + sign * (T / M)
print('S = ', s)