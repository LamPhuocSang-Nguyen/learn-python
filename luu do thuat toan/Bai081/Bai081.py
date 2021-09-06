x = eval(input('Enter x = '))
n = int(input('Enter n = '))
s = 1 / x
T = x
for i in range(1, n):
    T = T * (x + i)
    s = s + 1 / T
print('S = ', s)