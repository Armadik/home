#1
a = list('Python')
print(a)
y = a[::2]
print(y)

#2
l = (1, 5, 7, 1, 4, 6, 9)
for i in range(len(l)-1):
    v = i+1
    n = l[i]
    m = l[v]
    if m > n:
        #print(m)
        print(' ')
        
#3
var = [12, 3, 500, -3, 9, 2, 22, 1]
print(var)
ma = max(var)
mi = min(var)
imi = var.index(min(var))
ima = var.index(max(var))
var.remove(mi)
var.remove(ma)
var.insert(imi, ma)
var.insert(ima, mi)
print(var)
