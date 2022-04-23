import re 

#parse a file, extract all the numbers in the file, compute the sum of the numbers

fileName = input("Enter File Name: ")
handle = open(fileName)
lyst = []
for line in handle:
    #print(line)
    if not re.search("[0-9]", line):
        continue
    result = re.findall("[0-9]+",line)
    lyst.extend(result)
sum = 0
for i in lyst:
    i = int(i)
    sum += i

print(sum)