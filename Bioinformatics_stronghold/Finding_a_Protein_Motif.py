import sys
import re
from urllib.request import urlopen
from Bio import SeqIO

with open(sys.argv[1],"r") as f:
    data = f.readlines()

for line in data:
    fasta_data_handler = urlopen("http://www.uniprot.org/uniprot/" + line.rstrip() + ".fasta")
    fasta_data = fasta_data_handler.read().decode('utf-8', 'ignore')
    with open("seqs.fasta", "a") as f:
        f.write(fasta_data)

counter = 0
for record in SeqIO.parse(open("seqs.fasta", "r"), "fasta"):
    pos = []
    for hit in re.finditer( r'(?=(N[^P][ST][^P]))' , str(record.seq)):
        pos.append(hit.start()+1)
    if len(pos) > 0 :
        print(data[counter].rstrip())
        print(' '.join(map(str,pos)))
    counter +=1
