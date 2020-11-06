import re
import sys
from Bio import SeqIO                                     
from Bio.Seq import Seq                                   
                     

record = SeqIO.read(sys.argv[1], 'fasta')
pat = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
seq = record.seq
seq_rev = seq.reverse_complement()
sequences = []

for m in re.findall(pat, str(seq)):
    dna = Seq(m,)
    prot = dna.translate()
    if prot not in sequences:
        sequences.append(prot)
for n in re.findall(pat, str(seq_rev)):
    rev_dna = Seq(n,)
    rev_prot = rev_dna.translate()
    if rev_prot not in sequences:
        sequences.append(rev_prot)

for i, s in enumerate(sequences):
    print(s)