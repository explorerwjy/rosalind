class rosalind_perm:
	def __init__(self,handle):
		handle = open(handle)
		self.num = int(handle.readline().strip())
		self.numlist = [str(i) for i in range(1,self.num+1)]
		self.len = len(self.numlist)
		self.res = []

	def perm(self,res,k,m):
		if (k==m):
			self.res.append((' '.join(res)))
			return
		else:
			for j in range(k,m+1,1):
				res[j],res[k] = res[k],res[j]
				self.perm(res,k+1,m)
				res[j],res[k] = res[k],res[j]



if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_sign.txt'
	sol = rosalind_perm(small_input)
	sol.perm(sol.numlist,0,sol.len-1)
	print len(sol.res)
	for i in sol.res:
		print i


		
