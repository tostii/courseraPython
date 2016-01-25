# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.split()
    for word in line:
        try:
            pos = lst.index(word)
        except:
            lst.append(word)
lst.sort()
print(lst)
