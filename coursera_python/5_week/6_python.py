A = int(input())


def sum(c):
    c = 0
    l = []
    while c != A:
        d = input()
        c += 1
        l.append(d)
    return l


print(sum(A).count("0"))
