from fileinput import filename

fileName = input("Enter File Name: ")
handle = open(fileName)
dictCount = {}
count = 0

arr = []
for line in handle:
    words = line.split()
    for word in words: 
        arr.append(word)


print("Words: ", arr)

for word in arr:
    if word not in dictCount.keys():
        dictCount[word] = dictCount.get(word,1)
    else:
        dictCount[word] = dictCount.get(word) + 1

print(dictCount)
