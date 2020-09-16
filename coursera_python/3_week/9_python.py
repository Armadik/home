#x = float(input())
#r = float(input())
#k = float(input())
x = 12
r = 179
k = 0
gods = 5
za_god = 0
i = 0
cena = r + (k/100)
while i != gods:
    pribil = cena * (x / 100)
    print('{0:.2f}'.format(pribil))
    print(('{0:.2f}'.format(pribil % 1)))
    summa = cena + float(('{0:.2f}'.format(pribil)))
    print(cena + pribil)
    print(summa)
    cena = summa
    i += 1
print('----')
print(cena)
