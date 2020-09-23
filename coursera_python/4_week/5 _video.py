def sort2(a, b):
    if a < b:
        return a, b
    else:
        return b, a


a = int(input())
b = int(input())
minimum, maximum = sort2(a, b)
print(minimum, maximum)


def max2(a, b):
    if a > b:
        return a
    return b


def max3(a, b, c):
    return max2(max2(a, b), c)


def isEven(n):
    return n % 2 == 0


if isEven(n):
    print("EVEN")
else:
    print("ODD")
