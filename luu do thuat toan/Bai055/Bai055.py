n = int(input('Enter n = '))
T = 1
i = 1
while i <= n:
    if n % i == 0:
       T = T * i
    i = i + 2
print(T)