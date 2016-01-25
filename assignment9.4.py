name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

email = dict()
fh = open(name)


for line in fh:
    lst = line.split()
    try:
        if lst[0] == 'From':
            email[lst[1]] = email.get(lst[1],0) + 1
    except:
        continue

maxcount = None
maxword = None
for word,count in email.items():
    if maxcount is None or count > maxcount:
        maxword = word
        maxcount = count

print(maxword,maxcount)