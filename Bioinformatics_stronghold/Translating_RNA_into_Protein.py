import sys

with open(sys.argv[1], "r") as f:
    data = f.read()

rna_codons = {
'UUC' : 'F'   ,   'CUC' : 'L', 'AUC' : 'I', 'GUC' : 'V',
'UUU' : 'F'   ,   'CUU' : 'L', 'AUU' : 'I', 'GUU' : 'V',
'UUA' : 'L'   ,   'CUA' : 'L', 'AUA' : 'I', 'GUA' : 'V',
'UUG' : 'L'   ,   'CUG' : 'L', 'AUG' : 'M', 'GUG' : 'V',
'UCU' : 'S'   ,   'CCU' : 'P', 'ACU' : 'T', 'GCU' : 'A',
'UCC' : 'S'   ,   'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A',
'UCA' : 'S'   ,   'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A',
'UCG' : 'S'   ,   'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A',
'UAU' : 'Y'   ,   'CAU' : 'H', 'AAU' : 'N', 'GAU' : 'D',
'UAC' : 'Y'   ,   'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D',
'UAA' : 'Stop',   'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E',
'UAG' : 'Stop',   'CAG' : 'Q', 'AAG' : 'K', 'GAG' : 'E',
'UGU' : 'C'   ,   'CGU' : 'R', 'AGU' : 'S', 'GGU' : 'G',
'UGC' : 'C'   ,   'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G',
'UGA' : 'Stop',   'CGA' : 'R', 'AGA' : 'R', 'GGA' : 'G',
'UGG' : 'W'   ,   'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G'
}

prot = []
for i in range(0,len(data),3):
    codon = data[i] + data[i+1] + data[i+2]
    if rna_codons[codon] != 'Stop':
        prot.append(rna_codons[codon])
    else:
        break

print(''.join(prot))