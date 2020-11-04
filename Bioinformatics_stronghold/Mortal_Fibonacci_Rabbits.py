import sys

def mortal_fib(n, m):
    #Populate with zeros vector
    rabbits = [0] * m
    rabbits[-1] = 1
    for _ in range(1, n):
        new = sum(rabbits[:-1])
        rabbits[:-1] = rabbits[1:] 
        rabbits[-1] = new
    return sum(rabbits)

print(mortal_fib(int(sys.argv[1]),int(sys.argv[2]))) 