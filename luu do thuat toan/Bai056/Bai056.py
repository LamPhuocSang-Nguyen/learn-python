n = int(input('Enter n = '))
i = 2
s = 0
while i <= n:
    if n % i == 0:
        s = s + 1
    i = i + 2
print(s)