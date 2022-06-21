#recursive binary search 
def binarySearch(array, target):
    return rBSearchHelper(array, target, 0, len(array)-1)

def rBSearchHelper(array, target, left, right):
    #base case (only one item, left==right & target==mid)
    if left > right:
        return -1
        
    if left==right:
        if target == array[left]:
            return left
        else: 
            return -1
         
    else: 
        mid = (left + right)//2
        if array[mid] == target: 
            return mid
        if array[mid] > target: 
            return rBSearchHelper(array, target, left, mid-1)
        elif array[mid] < target: 
            return rBSearchHelper(array, target, mid+1, right)
            

print(binarySearch(array=[4,5,7,8,9,12], target=7))