a, b, c = int(input()), int(input()), int(input())
if a == min(a, b, c) and c == max(a, b, c):
    print(a, b, c)
elif c == min(a, b, c) and a == max(a, b, c):
    print(c, b, a)
elif b == min(a, b, c) and c == max(a, b, c):
    print(b, a, c)
elif b == min(a, b, c) and a == max(a, b, c):
    print(b, c, a)
elif b == max(a, b, c) and c == min(a, b, c):
    print(c, a, b)
elif b == max(a, b, c) and a == min(a, b, c):
    print(a, c, b)
