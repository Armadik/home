print('{0:.25f}'.format(0.1))
print(0.2.as_integer_ratio())
x = float(input())
y = float(input())
epsilon = 10 ** -6
if abs(x - y) < epsilon:
    print('Equal')
else:
    print('Not equal')