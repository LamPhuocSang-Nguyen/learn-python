n = int(input('Enter n = '))
i = 1
s = 0
while (i <= n):
    if n % i == 0:
        s = s + i
    i = i + 1
print('s = ', s)