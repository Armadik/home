#1
d = {'a': 1, 'b': 2, 'f': 4312, 's': 13}
print(d['b'])
#2
rd = {}
for k, v in d.items():
    rd[v] = rd.get(v, []) + [k]
#    print(rd)
#3
sp = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
dsp = dict.fromkeys(sp, 1)



