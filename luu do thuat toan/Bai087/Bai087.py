x = eval(input('Enter x = '))
n = int(input('Enter n = '))
s = x
T = x
sign = -1
for i in range(3, 2 * n + 2, 2):
    T = T * x * x 
    s = s + sign * T
    sign = -sign
print('S = ', s)