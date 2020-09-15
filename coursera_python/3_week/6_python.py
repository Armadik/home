x = float(input())
y = ('{0:.2f}'.format(x - int(x)))
if y[2::] == "00":
    print((int(x)), 0)
else:
    print((int(x)), (y[2::]))
