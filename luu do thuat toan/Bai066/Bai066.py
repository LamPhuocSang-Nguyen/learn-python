x = int(input('Enter n = '))
flag = False
t = x
while t != 0:
    dv = t % 10
    if dv % 2 == 0:
        flag = True
    t = t // 10

if flag:
    print('Exist the even number')
else:
    print('No exist')

