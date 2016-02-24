import sys
handle = open(sys.argv[1])
value = handle.read().split()
value = map(float,value)
off1 = value[0]*2
off2 = value[1]*2
off3 = value[2]*2
off4 = value[3]*2*(3.0/4)
off5 = value[4]*2*(1.0/2)
off6 = value[5]*0
#print off1,off2,off3,off4,off5,off6
print off1+off2+off3+off4+off5+off6
