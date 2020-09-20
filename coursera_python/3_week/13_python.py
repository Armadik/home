string = str(input())
p = string.find("h")
s = string[::-1].find("h")
if p and len(string) - s - 1 > 0:
    print(string[0:len(string) - s - 1], string[p + 1:-1], string[-1], sep='')
elif string[0] and string[-1] == "h":
    print(string)
    pass
else:
    pass
