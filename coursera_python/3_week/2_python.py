from math import sqrt
x = float(input())
y = float(input())
z = float(input())
p = float((x + y + z) / 2)
S = p*(p - x)*(p - y)*(p - z)
print('{0:.10f}'.format(sqrt(S)))
