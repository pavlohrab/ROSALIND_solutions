import sys

m = int(sys.argv[1])
p = int(sys.argv[2])

def rabits(m,p):
    if m <2:
        return m
    else:
        total = rabits(m-1,p) + p * rabits(m-2, p)
        return total    

print(rabits(m,p))