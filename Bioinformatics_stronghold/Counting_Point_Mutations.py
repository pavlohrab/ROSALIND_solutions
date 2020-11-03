import sys

def hamdist(seq1, seq2):
    dist = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            dist += 1
    return dist


with open(sys.argv[1], "r") as f :
    data = f.readlines()

print(hamdist(data[0], data[1]))

