now = int(input())
i = int(1)

while i <= now - 1:
    if i == 1:
        pass
    i = i * 2
if i == now:
    print('YES')
elif now == 1:
    print('YES')
else:
    print('NO')