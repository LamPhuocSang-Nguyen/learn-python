x = eval(input('Enter x = '))
n = int(input('Enter n = '))
s = 1
T = 1
for i in range(1, n + 1):
    T = T * x
    s = s + (i + 1) * T
print('S =', s)