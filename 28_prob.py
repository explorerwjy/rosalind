from math import log10
class rosalind_prob:
	def __init__(self,handle):
		handle = open(handle)
		self.seq = handle.readline().strip()
		self.num = [float(num) for num in handle.readline().strip().split()]

	def prob(self):
		B = []
		gc = self.seq.count('G')+self.seq.count('C')
		at = len(self.seq)-gc
		for x in self.num:
			yield round(log10((x/2)**gc*(0.5-x/2)**at),3)

if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_prob.txt'
	sol = rosalind_prob(large_input)
	for x in sol.prob():
		print x,