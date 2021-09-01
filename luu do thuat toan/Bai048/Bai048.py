x = int(input('Enter x = '))
n = int(input('Enter n = '))
T = 1
i = x
while (i <= (x + n)):
    T = T * i
    i = i + 1
print('T = ', T)