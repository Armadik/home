k = int(input())
if k == 1:
    print(k, "korova")
elif 4 >= k >= 2:
    print(k, 'korovy')
elif 20 >= k >= 5:
    print(k, 'korov')
elif k > 20:
    if (k % 10) == 1:
        print(k, "korova")
    elif 4 >= (k % 10) >= 2:
        print(k, 'korovy')
    elif 5 >= (k % 10) >= 9:
        print(k, 'korov')
    elif (k % 10) >= 0:
        print(k, 'korov')