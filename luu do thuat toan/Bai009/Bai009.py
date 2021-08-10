from math import pi,sin

radius = eval(input('Enter radius: '))

n = int(input('Enter n = '))

s = (1.0 / 2) * n * radius * radius * sin(2 * pi / n)

print('s = ', s)