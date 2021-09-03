x = int(input('Enter n = '))
T = 1
t = x
while t != 0:
    dv = t % 10
    if dv % 2 == 1:
        T = T * dv
    t = t // 10
print('T = ', T)