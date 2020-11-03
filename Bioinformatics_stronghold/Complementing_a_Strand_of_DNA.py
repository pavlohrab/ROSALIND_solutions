import sys

def reverse(s):
    """
    This function reverses the given string
    """
    return s[::-1]

with open(sys.argv[1], "r") as f:
    data = f.read().upper().strip()

DNA_alphabet = {
    'A' :'T',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C'
}

rev_data = reverse(data)
new_data = ""
for i in rev_data:
    new_data = new_data + DNA_alphabet[i]

print(new_data)