from sys import argv

hand1 = open(argv[1])
hand2 = open(argv[2])

prt = hand1.readline().strip()
prt = list(prt)
dic = {}
for l in hand2:
	p,w = l.split()
	dic[p] = w
sum = 0
for i in prt:
	sum += float(dic[i])
print round(sum,3)
