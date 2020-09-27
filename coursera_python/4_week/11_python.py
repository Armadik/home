def sum(c, n):
    if n == 0:
        return c
    else:
        return sum(c + 1, n - 1)


a = float(input())
b = float(input())

print(int(sum(a, b)))