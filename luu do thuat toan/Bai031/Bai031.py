n = int(input('Enter n = '))

i = 1

s = 0

while(i <= (2 * n + 1)):
    s = s + (1.0 / i)
    i = i + 2

print('s = ', s)