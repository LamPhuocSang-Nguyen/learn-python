x = int(input('Enter n = '))
t = x
min = t % 10
while t != 0:
    dv = t % 10
    if dv < min:
        min = dv
    t = t // 10
print('min = ', min)