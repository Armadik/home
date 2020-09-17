string = str(input())
obr = string[::-1]
pos = string.find("f")
sop = obr.find("f")
if pos == len(string) - sop - 1:
    print(pos)
elif pos == -1:
    pass
else:
    print(pos, len(string) - sop - 1)
