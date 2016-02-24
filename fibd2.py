import sys
generations = [1, 1] #Seed the sequence with the 1 pair, then in their reproductive month.
def fib(i, j):
	count = 2
    while (count < i):
        if (count < j):
            generations.append(generations[-2] + generations[-1]) #recurrence relation before rabbits start dying (simply fib seq Fn = Fn-2 + Fn-1)
        elif (count == j or count == j+1):
            print ("in base cases for newborns (1st+2nd gen. deaths)") #Base cases for subtracting rabbit deaths (1 death in first 2 death gens)
            generations.append((generations[-2] + generations[-1]) - 1)#Fn = Fn-2 + Fn-1 - 1
        else:
            generations.append((generations[-2] + generations[-1]) - (generations[-(j+1)])) #Our recurrence relation here is Fn-2 + Fn-1 - Fn-(j+1)
        count += 1
    return (generations[-1])

handle = open(sys.argv[1])
n,k = handle.read().split()
print fib(int(n),int(k))

