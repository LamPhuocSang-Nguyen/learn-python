x = int(input('Enter n = '))
s = 0
t = x
while t != 0:
    dv = t % 10
    if dv % 2 == 0:
        s = s + dv
    t = t // 10
print('s = ', s)