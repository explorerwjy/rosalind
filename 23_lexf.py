from sys import argv

class LEXF:
	def lexf(self,alphabet,n,per,res):
		if n == 0:
			res.append(per)
		else:
			for alpha in alphabet:
				self.lexf(alphabet,n-1,per+alpha,res)
		return res

if __name__=='__main__':
	handle = open(argv[1])
	alphabet = handle.readline().split()
	n = int(handle.readline().strip())
	my_lexf = LEXF()
	res = my_lexf.lexf(alphabet,n,"",[])
	for i in res:
		print i
