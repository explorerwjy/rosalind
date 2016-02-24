import sys
import Bio.SeqIO

def first(x):
    return x[:3]
def last(x):
    return x[-3:]

handle = open(sys.argv[1])
nodes = []
for record in Bio.SeqIO.parse(handle,"fasta"):
    nodes.append(record)

for i,record1 in enumerate(nodes):
    #print first(record.seq)
    #print last(record.seq)
    for record2 in nodes[i+1:]:
        if first(record1.seq) == last(record2.seq):
            print record2.id,record1.id
        elif first(record2.seq) == last(record1.seq):
            print record1.id,record2.id
