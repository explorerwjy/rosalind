import sys
handle = open(sys.argv[1])

str1,str2 = handle.read().split()

def substr(str1,str2):
    positions = []
    for i in range(0,len(str1)-len(str2)):
        if str1[i:len(str2)+i]==str2:
            positions.append(i+1)
    return positions

p = substr(str1,str2)
for i in p:
    print i,
