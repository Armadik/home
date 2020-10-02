def power(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return power(n-1, k-1) + power(n-1, k)


a = float(input())
b = float(input())

print(power(a, b))
