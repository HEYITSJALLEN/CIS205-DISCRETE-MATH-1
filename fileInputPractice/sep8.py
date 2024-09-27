filename = "names.txt"
file = open(filename)
lines = file.readlines()
for line in lines:
    line = line.rstrip()
    print(line + "'s favorite class is CIS205")