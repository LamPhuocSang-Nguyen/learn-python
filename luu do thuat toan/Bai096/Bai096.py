from math import sqrt
n = int(input())
s = 0
T = 1
for i in range(1,n+1):
    T = T * i
    s = sqrt(s + T)
print(s)