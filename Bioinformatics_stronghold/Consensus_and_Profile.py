import sys
from Bio import SeqIO

A, T, C, G = [], [], [], []

consensus = ""
close = 0
for record in SeqIO.parse(open(sys.argv[1], "r"), "fasta"):
    if close == 0:
        seq = record.seq
        close += 1
    else:
        break

for i in range(len(seq)):
    Count = { "A" :0, "C" : 0, "T" : 0, "G" : 0}
    for record in SeqIO.parse(open(sys.argv[1], "r"), "fasta"):
        if record.seq[i] in Count:
            Count[record.seq[i]] += 1
        
    A.append(Count["A"])
    C.append(Count["C"])
    T.append(Count["T"])
    G.append(Count["G"])

    consensus = consensus + max(Count, key=Count.get)

print(consensus)
print("A: " + " ".join(map(str,A)))
print("T: " + " ".join(map(str, T)))
print("C: " + " ".join(map(str, C)))
print("G: " + " ".join(map(str, G)))


