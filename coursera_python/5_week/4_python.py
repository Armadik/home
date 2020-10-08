A = int(input())


def summ(n):
    if n == 0:
        return n ** 2
    else:
        return n ** 2 + summ(n-1)


print(summ(A))
