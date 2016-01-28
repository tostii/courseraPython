name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.split()
    try:
        if line[0] == "From":
            line = line[5].split(":")
            counts[line[0]] = counts.get(line[0],0) + 1
    except:
        continue
for k, v in sorted(counts.items()):
    print(k,v)
