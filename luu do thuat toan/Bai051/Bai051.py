n = int(input('Enter n = '))
i = 1
T = 1
while i <= n:
    if n % i == 0:
        T = T * i
    i = i + 1
print('T = ', T)