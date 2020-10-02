def power(n):
    n = int(input())
    if n == 0:
        return n
    else:
        return n + power(n)


print(power(0))
