def power(c, n):
    if n == 0:
        return 1
    else:
        return c * power(c, n - 1)


a = float(input())
b = float(input())

print(power(a, b))
