n = int(input('Enter n = '))

i = 2

s = 0
while(i <= (2 * n)):
    s = s + 1.0 / i
    i = i + 2

print('s = ', s)