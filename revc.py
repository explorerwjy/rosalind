from sys import argv
seq = "".join(file(argv[1]).read().split())
dic = {"A":"T",'T':'A','C':'G','G':'C'}
comp = []
for ch in seq:
	comp.append(dic.get(ch))
print ''.join(comp)[::-1]
