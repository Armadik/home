string = str(input())
obr = string[::-1]
pos = string.find("h")
sop = obr.find("h")
if pos and len(string) - sop - 1 > 0:
    print(string[0:pos], string[(len(string) - sop):-1], string[-1], sep='')
elif pos == -1:
    pass
else:
    pass
