def power(c, n):
    if c % n == 0:
        return print(int(a / n), int(b / n))
    else:
        return power(n, c % n)


a = float(input())
b = float(input())

power(a, b)
