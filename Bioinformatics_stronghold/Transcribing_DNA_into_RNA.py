import sys

with open(sys.argv[1], "r") as f:
    data = f.read().upper().strip()

print(data.replace('T', 'U'))