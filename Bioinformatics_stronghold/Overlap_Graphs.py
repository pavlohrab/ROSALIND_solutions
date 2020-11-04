import sys
from Bio import SeqIO

seqs = [record for record in SeqIO.parse(open(sys.argv[1], "r"), "fasta")]

for i in range(len(seqs)):
    suf = seqs[i].seq[-3:]
    for j in range(len(seqs)):
        if suf == seqs[j].seq[:3]:
            if seqs[i].id == seqs[j].id:
                pass
            else:
                print(seqs[i].id, seqs[j].id)