x = eval(input('Enter x = '))
n = int(input('Enter n = '))
S = 0
T = 1
for i in range(2, 2 * n + 1, 2):
    T = T * x * x 
    S = S + T
print('S = ', S)

