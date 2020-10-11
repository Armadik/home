A = int(input())

print("+___ " * A)
for i in range(1, A + 1):

    print("|" + str(i) + " / ", sep="", end="")
print()
print("|__\\ " * A)
print("|    " * A)