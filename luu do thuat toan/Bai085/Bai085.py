x = eval(input('Enter x = '))
n = int(input('Enter n = '))
s = 0
T = 1
sign = 1
for i in range(n):
    T = T * x
    s = s + sign * T
    sign = -sign
print('S = ', s)