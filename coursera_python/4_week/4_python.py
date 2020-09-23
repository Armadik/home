from math import sqrt


def distance(x1, y1, x2, y2):
    rasstoy = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return '{0:.10f}'.format(rasstoy)


def perimeter(p):
    a = (distance(x_1, y_1, x_2, y_2))
    b = (distance(x_2, y_2, x_3, y_3))
    c = (distance(x_1, y_1, x_3, y_3))
    print(float(a) + float(b) + float(c))


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())

perimeter(0)
