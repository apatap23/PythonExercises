name = input("Enter file:")
handle = open(name)

arr = []
dictCount = {}

for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5]
    timeSplit = time.split(':')
    hour = timeSplit[0]
    arr.append(hour)

for hour in arr:
    dictCount[hour] = dictCount.get(hour, 0) + 1


for k,v in sorted(dictCount.items()):
    print(k,v)
