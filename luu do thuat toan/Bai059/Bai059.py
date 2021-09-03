x = int(input('Enter n = '))
dem = 0
t = x
while t != 0:
    dem = dem + 1
    t = t // 10
print('dem = ', dem)