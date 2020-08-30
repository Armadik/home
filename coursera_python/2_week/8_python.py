x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if 7 >= x1 >= 1 and 8 >= x2 >= 1 and 7 >= y1 >= 1 and 8 >= y2 >= 1 and y2 > y1:
    if ((x1 + 1) % 2 != 0) and (x2 % 2 != 0):
        if ((y1 + 1) % 2 != 0) and (y2 % 2 != 0):
            print('YES')
        else:
            print('NO')
    elif ((x1 + 1) % 2 == 0) and (x2 % 2 == 0):
        if ((y1 + 1) % 2 == 0) and (y2 % 2 == 0):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')