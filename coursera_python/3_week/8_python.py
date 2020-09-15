x = float(input())
r = float(input())
k = float(input())
cena = r + (k/100)
pribil = cena * (x / 100)
summa = cena + pribil
kopeek = (summa % 1) * 100
ruble = int(summa)
print(ruble, '{0:.0f}'.format(kopeek))
