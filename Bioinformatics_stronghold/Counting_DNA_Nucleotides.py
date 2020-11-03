import sys

with open(sys.argv[1], "r") as f :
    data = f.read().upper()

As = str(data.count('A'))
Cs = str(data.count('C'))
Gs = str(data.count('G'))
Ts = str(data.count('T'))

print(As+" "+Cs+" "+Gs+" "+Ts)