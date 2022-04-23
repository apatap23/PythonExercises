fname = input("Enter file name: ")
handle = open(fname)
count = 0 
for line in handle:
    if line.startswith('From'):
        line = line.strip()
        count += 1
        splitLine = line.split()
        address = splitLine[1]
        print(address)


print("There were", count, "lines in the file with From as the first word")






"""
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip().split()
    for i in words:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)
"""