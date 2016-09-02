#Solution
from Bio import SeqIO
from sys import argv

class LEXV():
	def __init__(self,alphabet,number):
		self.alphabet = alphabet
		self.number = int(number)

	def lexv(self):


if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_kmp.txt'
	alphabet,number = open(small_input,'r').read().split('\n')
	alphabet = alphabet.split(' ')
	print alphabet
	print number
	sol = LEXV(alphabet,number)
	sol.lexv()



