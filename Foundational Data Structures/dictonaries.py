"""
months = {}

months = {1: "Jan", 2: "Feb", 3:"Mar", 4:"April", 5: "May"}

rand = {"Amy": 1, "Suzuki":4, "Cello":10, "Fanta": -1}

del(months[1])
print(months)
print(months.keys())

months[1] = "Jan"
print(months)

for i,j in months.items():
    print(i,j)
"""

line = input("Enter Line: ")
dictCount = {}
count = 0

words = line.split()
print("Words: ", words)

for word in words:
    if word not in dictCount.keys():
        dictCount[word] = dictCount.get(word,1)
    else:
        dictCount[word] = dictCount.get(word) + 1

max = 0

for key in dictCount:
    if dictCount[key] > max: 
        max = dictCount.get(key)
        i,j = dictCount.items[key]
print(max)
print(dictCount)
dictCount.v