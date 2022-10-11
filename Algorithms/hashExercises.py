def removeDuplicate(input):
    res = []
    for i in input:
        if i.casefold() not in res:
            res.append(i.casefold())
    return res

def highestSkillOverlap(fellowSkills):
    dictFellowCount = dict()
    for x,y in fellowSkills.items():
        dictFellowCount[y] = dictFellowCount.get(y,0) + 1
    return max(dictFellowCount.keys())
        

def fewerThanTargetDistinct(input, target):
    inSet = set(input)
    if len(inSet) < target:
        return True
    else:
        return False
        
def numUniques(array: [int])-> int:
    countDict = dict()
    for i in array:
        countDict[i]=countDict.get(i,0)+1
    ansCount = 0
    for num, count in countDict.items():
        if count == 1:
            ansCount += 1
    return ansCount

    

    
print(removeDuplicate(["oliver","pixel","Pinky","oliver","pinky"]))
print(highestSkillOverlap({"oliver": 3, "pixel": 1, "pinky": 3}))
print(fewerThanTargetDistinct([1, 2, 2, 3, 3], 4 ))
print(fewerThanTargetDistinct([1, 2, 2, 3, 3], 3 ))
print(numUniques([])) # 0
print(numUniques([3, 1, 1, 2, 3, 1, 1, 1, 4])) # 2
print(numUniques([1])) # 1

