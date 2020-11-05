import sys
from Bio import SeqIO
import operator

freq_dict = {}
seqs = []
for record in SeqIO.parse(open(sys.argv[1], "r"), "fasta"):
    seqs.append(record.seq)
    
search_seq = seqs.pop()

def lcs(s1, s2):
    tmp_dict = {}
    for i in range(len(s1)):
        for j in range(len(s2)):
            if (s1[i] == s2[j]):
               # print(s1[i:], s2[j:])
                substring = s2[j]
                tmp_dict[substring] = 1
                end_of_string = min(len(s1)-i, len(s2)-j)
                for v in range(1, end_of_string):
                    if s1[i+v] == s2[j+v]:
                        #print("HIT: ", s1[i],  s1[i+v], s2[j], s2[j+v], v)
                        substring = substring + s2[j+v]
                        tmp_dict[substring] = 1
                    else:
                        tmp_dict[substring] = 1
                        break
                tmp_dict[substring] = 1
    return tmp_dict
counter = 1
for seq in seqs:
    print(counter)
    tmp_dict = lcs(search_seq, seq)
    for k,v in tmp_dict.items():
        if k in freq_dict:
            freq_dict[k] += 1
        else:
            freq_dict[k] = 1
    counter += 1

tmp_dict = {}
for k, v in freq_dict.items():
    if v == len(seqs):
        tmp_dict[k] = len(k)
answer = max(tmp_dict.items(), key=operator.itemgetter(1))[0]
#print(freq_dict)
#print(tmp_dict)
print(answer)