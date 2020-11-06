import sys
from itertools import permutations 

perms = []
perm = permutations(range(1,int(sys.argv[1])+1)) 

count = 0
for i in list(perm): 
    perms.append(i) 
    count += 1

print(count)
for i in perms:
    print(" ".join(map(str,i)))