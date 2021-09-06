x = eval(input('Enter x = '))
n = int(input('Enter n = '))
s = 1 + x
T = x
M = 1
for i in range(3, 2 * n + 2, 2):
    T = T * x * x
    M = M * (i - 1) * i
    s = s + T / M
print('S = ', s)