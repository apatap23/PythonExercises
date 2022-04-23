

while True: 
    try:
        fileName = input("Enter File Name: ")
        handle = open(fileName)
    except:
        print("File does not exist")
    else:
        count = 0
        for i in handle:
            count += 1
            i = i.strip()
            print(count, i)

        break
