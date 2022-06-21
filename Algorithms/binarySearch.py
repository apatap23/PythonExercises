#looking for target value in a sorted array 


#given: array of nums, target 
def binarySearch(arr, target):
    #sort array
    #print(type(arr))
    arr.sort()
    #print(type(arr))
    print(arr)
    #establish left, right, mid
    left = arr[0]
    right = arr[len(arr)-1]
    mid = arr[len(arr)//2]
    print("Mid: ", mid)
    #is the mid target?
    while len(arr) != 0: 
        if mid == target:
            return arr.index(mid)
            break
        #if mid is greater than target, then cut off mid through right 
        #move right to mid index and find new mid 

        elif mid > target: 
            right = mid
            newMidIndex = (arr.index(right) - arr.index(left))//2
            mid = arr[newMidIndex]
            print("Mid: ", mid)
        elif mid < target:
            left = mid
            tempArr = arr[left-1:]
            print(tempArr)
            newMidIndex = (tempArr.index(right) - tempArr.index(left))
            mid = tempArr[newMidIndex]
    if len(arr) == 0: 
        return -1


print(binarySearch([5,3,1,2,6],5))



