def sumUp(*nums):
    arr = list()
    sum = 0
    for i in nums:
        sum += int(i)
    
    print(f'The Sum is {sum}')

sumUp(1,2,3)