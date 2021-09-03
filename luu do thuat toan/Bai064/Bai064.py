x = int(input('Enter n = '))
max = 0
t = x
while t != 0:
    dv = t % 10
    if dv > max:
        max = dv
    t = t // 10
print('max = ', max)