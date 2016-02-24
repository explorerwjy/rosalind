from sys import argv
n,k = map(int,file(argv[1]).read().split())
i = 1
res,res_1,res_2 = 0,0,0
while i <= n:
	if i == 1:
		res = 1
	elif i == 2:
		res_1 = res
		res_2 = 0
		res = res_1 + res_2
	else:
		res_2 = res_1
		res_1 = res
		res = res_2 * k + res_1
	i += 1
print res
