import sys

with open(sys.argv[1], "r") as f:
    data = f.readlines()
string = data[0]
substring = data[1]

def find_substring(s,t):
    locations = []
    for i in range(len(s) - len(t) +1):
        location = s.find(t, i, i+len(t))
        if location != -1:
            locations.append(str(location+1))
    return locations

locations = find_substring(string, substring)

print(' '.join(locations))