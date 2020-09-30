def power(c, n):
    if c % n == 0:
        return n
    else:
        return power(n, c % n)


a = float(input())
b = float(input())

if a > b:
    print(int(power(b, a)))
else:
    print(int(power(a, b)))
