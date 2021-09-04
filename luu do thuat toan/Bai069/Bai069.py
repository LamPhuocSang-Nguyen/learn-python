x = eval(input('Enter x = '))
n = int(input('Enter n = '))
T = 1
S = 0
for i in range(n):
    T = T * x
    S = S + T
print('S = ', S)