import math

x1 = float(input('Enter x1: '))

y1 = float(input('Enter y1: '))

x2 = float(input('Enter x2: '))

y2 = float(input('Enter y2: '))

d = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

print('Distance is ', d)
