from math import factorial
from sys import argv

class PPER:
	def pper(self,n,m):
		return (factorial(n)/factorial(n-m))%1000000

if __name__=="__main__":
	n,m = map(int,open(argv[1]).read().split())
	my_pper = PPER()
	print my_pper.pper(n,m)
