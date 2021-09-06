x = eval(input('Enter x = '))
n = int(input('Enter n = '))
s = 0
T = 1
M = 1
for i in range(1, n + 1):
    T = T * x
    M = M * i
    s = s + T / M
print('S = ', s)