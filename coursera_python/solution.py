#x = float(input())
#r = float(input())
#k = float(input())
x = 12
r = 179
k = 0
gods = 5
za_god = 0
i = 0
while i != gods:
    cena = r + (k/100)
    print(cena)
    pribil = cena * (x / 100)
    print(pribil)
    summa = cena + pribil
    print(summa)
    i += 1
    cena += summa
    print(cena)

#kopeek = (summa % 1) * 100
#ruble = int(summa)
#za_god = ruble + (summa % 1)


