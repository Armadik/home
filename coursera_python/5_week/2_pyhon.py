A = int(input())
B = int(input())


if B > A:
    for i in range(A - 1, B):
        print(i + 1, end=' ')
else:
    for i in range(A, B-1, -1):
        print(i, end=' ')
