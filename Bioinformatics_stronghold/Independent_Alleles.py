import math 
import sys

k = int(sys.argv[1])
N = int(sys.argv[2])

P = 2**k                                                                       
prob = 0                                                                
for i in range(N, P + 1):                                                      
    prob_indiv = (math.factorial(P) /(math.factorial(i) * math.factorial(P - i))) * (0.25**i) * (0.75**(P - i))                                                        
    prob += prob_indiv                                                        
print(prob)         