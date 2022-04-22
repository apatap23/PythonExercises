import time 

userNum = input("Enter a number: ")

userNum = int(userNum)

while userNum > 0: 
    print(userNum)
    time.sleep(1)
    userNum -= 1
print("Blastoff!")
