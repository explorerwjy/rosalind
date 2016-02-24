from sys import argv
seq = "".join(file(argv[1]).read().split())
print seq.replace('T','U')

