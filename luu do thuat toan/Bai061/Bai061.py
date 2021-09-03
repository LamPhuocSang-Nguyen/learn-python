x = int(input('Enter n = '))
dem = 0
t = x
while t != 0:
    dv = t % 10
    if dv % 2 == 1:
        dem = dem + 1
    t = t // 10
print('s = ', dem)