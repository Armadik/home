def power(n):
    if n in (1, 2):
        return 1
    else:
        return power(n - 1) + power(n - 2)


a = float(input())

print(power(a))
