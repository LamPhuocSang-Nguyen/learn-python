n = int(input('Enter n = '))
Dem = 0
i = 1
while i <= n:
    if n % i == 0:
        Dem = Dem + 1
    i = i + 1
print('So luong uoc so la: ', Dem)