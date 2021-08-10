from math import pi, sin

radius = eval(input('Enter radius = '))

n = int(input('Enter n = '))

P = 2 * n * radius * sin(pi / n)

print('perimeter is ', P)