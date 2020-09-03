a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
g = int(input())

if b > a:
    if b > c:
        if c > a:
            (b, c, a) = (c,  b, a)
        elif a > c:
            (a, c, b) = (c, b, a)
if c > a:
    if c > b:
        if b > a:
            (c, b, a) = (c,  b, a)
        elif a > c:
            (c, a, b) = (c, b, a)
if a > b:
    if a > c:
        if b > c:
            (a, b, c) = (c, b, a)

if e > d:
    if e > g:
        if g > d:
            (e, g, d) = (g,  e, d)
        elif d > g:
            (d, g, e) = (g, e, d)
if g > d:
    if g > e:
        if e > d:
            (g, e, d) = (g,  e, d)
        elif d > g:
            (g, d, e) = (g, e, d)
if d > e:
    if d > g:
        if e > g:
            (d, e, g) = (g, e, d)

if (a + b + c) == (d + e + g):
    print("Boxes are equal")
elif b >= e and c >= g:
    print("The first box is larger than the second one")
elif b <= e and c <= g:
    print('The first box is smaller than the second one')
else:
    print("Boxes are incomparable")
