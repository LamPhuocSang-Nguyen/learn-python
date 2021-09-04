x = eval(input('Enter x = '))
n = int(input('Enter n = '))
S = 0
M = 0
T = 1
for i in range(1, n + 1):
    M = M + i
    T = T * x
    S = S + (T / M)
print('S = ', S)