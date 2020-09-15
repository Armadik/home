x = float(input())
i = 1
sumSeq = 0
while i != x + 1:
    sumSeq += (1/i**2)
    i += 1
print(sumSeq)