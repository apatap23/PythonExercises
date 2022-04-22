fname = input("Enter file name: ")
fh = open(fname)
count = 0
value = 0 
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find('0')
    val = float(line[pos:])
    value += val 
    count +=1
    print(value)
avg = value/count
print("Average spam confidence:", avg)

