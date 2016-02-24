from sys import argv
seq = "".join(file(argv[1]).read().split())
print seq.count('A'),seq.count('C'),seq.count('G'),seq.count('T')
