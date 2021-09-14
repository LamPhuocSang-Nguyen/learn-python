from math import sqrt
n = int(input("Enter n ="))
s = 0
for i in range(n, 0, -1):
    s = sqrt(i + s)
print("S = ", s)