import random 

#function chooses a random int between 0 and 100 (inclusive). 
#Asks user to guess what number has been choose
#program tells if too high, low, or right
#if right, program exits or let's user try again 
def guessing_game():
    number = random.randint(0,100)
    while True:
        userInput = int(input("Guess a Number: "))
        if userInput == number: 
            print("That's Correct!")
            quit()
        elif userInput > number:
            print("Too Large!")
            continue 
        elif userInput < number: 
            print("Too Small!")
            continue 
    
guessing_game()