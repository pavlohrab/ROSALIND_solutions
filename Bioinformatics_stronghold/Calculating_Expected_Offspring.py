import sys

with open(sys.argv[1], "r") as f:
    data =[float(x) for x in f.readline().split()]

prob = [1.0,1.0,1.0, 0.75,0.5,0]

solution = 0
for i in range(len(data)):
    solution += 2*data[i]*prob[i]

print(solution)
