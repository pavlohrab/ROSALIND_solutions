import sys

with open(sys.argv[1], "r") as f:
    protein = f.read()

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
 
aa_freqs = {}
for k,v in rna_codons.items():
    if v in aa_freqs:
        aa_freqs[v] += 1
    else:
        aa_freqs[v] = 1

n = 1
n *= aa_freqs['Stop']
for char in protein:
    n *= aa_freqs[char]


print(n % 1000000)

