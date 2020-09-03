v = 3
f = 5
k = int(input())
if v % f == 0 or f % v == 0:
    print('YES')
elif (k % f) % v == 0 or (k % v) % f == 0:
    print('YES')
else:
    print('NO')
