A = int(input())
nach = int((str(1) + (A * "0")))
m_nach = int((str(1) + ((A - 1) * "0")))

if A > 0:
    for i in range(nach, m_nach, -2):
        print(i - 1, end=' ')
elif A == 0:
    pass
