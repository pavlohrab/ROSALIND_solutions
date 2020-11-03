import sys
from Bio import SeqIO

def GC_count(seq):
    Cs = seq.count("C")
    Gs = seq.count("G")
    GC = Cs + Gs
    return GC/len(seq)

GCs = {}

for record in SeqIO.parse(open(sys.argv[1], "r"), "fasta"):
    GCs[record.id] = GC_count(record.seq)

max_GC_for_comparison =  max(GCs.values())
max_GC = str(max(GCs.values())*100)
max_name = ''.join([k for k,v in GCs.items() if v == max_GC_for_comparison ])
print(max_name + "\n" + max_GC )
