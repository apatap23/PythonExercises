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
        

print(removeDuplicate(["oliver","pixel","Pinky","oliver","pinky"]))
print(highestSkillOverlap({"oliver": 3, "pixel": 1, "pinky": 3}))
print(fewerThanTargetDistinct([1, 2, 2, 3, 3], 4 ))
print(fewerThanTargetDistinct([1, 2, 2, 3, 3], 3 ))
