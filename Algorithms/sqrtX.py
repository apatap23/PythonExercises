#given: non-negative integer x 
#expected output: sqrt of x (truncate the decimal digits and return only the integer part)

def findSqrt(value):
    arrPerfectSquares = [i*i for i in range(1,46339)]

    left = 0
    right = len(arrPerfectSquares)-1
    mid = (left + right)//2

    #check if mid*mid 


 