x = eval(input('Enter x = '))
n = int(input('Enter n = '))
S = x
T = x
for i in range(3, n * 2 + 2, 2):
    T = T * x * x
    S = S + T
print('S = ', S)