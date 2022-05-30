def insertSort(takeString): 
    arr = [21,11,4,32,33,53,2,5,1]

    iter = 0 
    
    while iter <= len(arr):
        for i in range(iter):
            if arr[i] < arr[i - 1]:
                temp = arr[i]
                arr[i] = arr[i -1]
                arr[i-1] = temp
            else: 
                iter += 1
    print(arr)
                
insertSort("string")

