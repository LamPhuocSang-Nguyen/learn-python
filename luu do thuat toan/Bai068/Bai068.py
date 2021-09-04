n = int(input('Enter n = '))
T = 1
S = 0
for i in range(1,n + 1):
    T = T * i
    S = S + T
print('S = ', S)
