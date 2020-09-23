from math import sqrt


def distance(x1, y1, x2, y2):
    rasstoy = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print('{0:.10f}'.format(rasstoy))


a = float(input())
b = float(input())
c = float(input())
d = float(input())

distance(a, b, c, d)
