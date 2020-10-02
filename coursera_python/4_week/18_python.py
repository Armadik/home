def power(n):
    n = int(input())
    if n != 0:
        power(n)
        print(n)
    else:
        print(n)


power(0)