from sys import argv
def factorial(start,stop):
	res = 1
	while start >= stop:
		res *= start
		start -= 1
	return res

def combine(m,n):
	return (factorial(n,n-m+1)+0.0)/(factorial(m,1))

k,m,n = map(int,file(argv[1]).read().split())
print "%.5f"%(combine(2,k)/combine(2,k+m+n)+combine(1,k)*combine(1,m)/combine(2,k+n+m)+combine(1,k)*combine(1,n)/combine(2,k+m+n)+combine(1,m)*combine(1,n)/combine(2,k+m+n)*0.5+combine(2,m)/combine(2,k+m+n)*3/4)
