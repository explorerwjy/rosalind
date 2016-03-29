class rosalind_sign:
	def __init__(self,handle):
		handle = open(handle)
		self.num = int(handle.readline().strip())
		self.numlist = [str(i) for i in range(1,self.num+1)]
		self.len = len(self.numlist)
		self.res = []
		self.signs = ['+','-']

	def perm(self,res,k,m):
		if (k==m):
			self.res.append((' '.join(res)))
			return
		else:
			for j in range(k,m+1,1):
				res[j],res[k] = res[k],res[j]
				self.perm(res,k+1,m)
				res[j],res[k] = res[k],res[j]

	def sign(self):
		for i in range(1,self.len):
			tmp = []
			for j in range(0,len(self.signs)):
				tmp.append(self.signs[j]+'+')
				tmp.append(self.signs[j]+'-')
			self.signs = tmp

	def changesign(self,i):
		if i == '+':
			return ''
		else:
			return i

	def combine(self):
		for i in self.res: #nums
			for j in self.signs: #signs
				sign = [self.changesign(s) for s in list(j)]
				num = [n for n in i.split(' ')]
				tmp = []
				for k in range(self.num):
					tmp.append(sign[k]+num[k])
				yield ' '.join(tmp)

if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_sign.txt'
	sol = rosalind_sign(large_input)
	sol.perm(sol.numlist,0,sol.len-1)
	sol.sign()
	print len(sol.res)*len(sol.signs)
	for i in sol.combine():
		print i
	
