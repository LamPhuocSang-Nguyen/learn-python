from math import sqrt,pow

x1 = eval(input('x1 = '))

y1 = eval(input('y1 = '))

x2 = eval(input('x2 = '))

y2 = eval(input('y2 = '))

x3 = eval(input('x3 = '))

y3 = eval(input('y3 = '))

ab = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

ac = sqrt(pow((x3 - x1), 2) + pow((y3 - y1), 2))

bc = sqrt(pow((x3 - x2), 2) + pow((y3 - y2), 2))

p = (ab + ac + bc) / 2.0

s = sqrt(p * (p - ab) * (p - ac) * (p - bc))

print('area is ', s)