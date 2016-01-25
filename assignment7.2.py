# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
curr = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(":")
    line = float(line[pos+1:].strip())
    curr = curr + line
    count = count + 1

print("Average spam confidence:",curr/count)
