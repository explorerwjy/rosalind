from sys import argv

def longer(seq1,seq2):
	if len(seq1)>len(seq2):
		return seq1
	else:
		return seq2

def incs(inc,new):
	res = [new]
	for seq in inc:
		tmp = seq[:]
		if new > tmp[-1]:
			tmp.append(new)
			res = longer(res,tmp)
	return res,len(res)

def decs(dec,new):
	res = [new]
	for seq in dec:
		tmp = seq[:]
		if new < tmp[-1]:
			tmp.append(new)
			res = longer(res,tmp)
	return res,len(res)

handle = open(argv[1])
n = int(handle.readline())
nums = map(int,handle.readline().split())
inc = [[nums[0]]]
dec = [[nums[0]]]
l_inc = 1
i_index = 0
l_dec = 1
d_index = 0
for i in xrange(1,n):
	new_inc,length = incs(inc,nums[i])
	inc.append(new_inc)
	if length > l_inc:
		l_inc = length
		i_index = i
	
	new_dec,length = decs(dec,nums[i])
	dec.append(new_dec)
	if length > l_dec:
		l_dec = length
		d_index = i

#print inc[i_index]
#print dec[d_index]
for i in inc[i_index]:
	print i,
print
for i in dec[d_index]:
	print i,
print
