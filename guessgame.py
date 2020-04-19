import random
print("Welcome to Guess Game with 3 levels: Hard, Medium and Easy")
level = input("Enter your preferred level ")
if level.upper() == "EASY":
    ranNum = random.randint(1,10)
    i = 0
    while i<6:
        choiceNum = input("Enter your guess between 1 and 10 ")
        if ranNum == int(choiceNum):
            print("You got it right")
            break
        if ranNum != int(choiceNum):
            input ("That was wrong, you have "+str(5-i)+" guesses left")
        i +=1
    if int(choiceNum) == ranNum:
        print("BRAVO!!! You win")
    if  int(choiceNum) != ranNum:
        print("GAME OVER!!!")

if level.upper() == "MEDIUM":
    ranNum = random.randint(1,20)
    i = 0
    while i < 4:
        choiceNum = input("Enter your guess between 1 and 20 ")
        if ranNum == int(choiceNum):
            print("You got it right")
            break
        if ranNum != int(choiceNum):
            input ("That was wrong, you have "+str(3-i)+" guesses left")
        i +=1
    if int(choiceNum) == ranNum:
        print("BRAVO!!! You win")
    if int(choiceNum) != ranNum:
        print("GAME OVER!!!")

if level.upper() == "HARD":
    ranNum = random.randint(1,50)

    i = 0
    while i<3:
        choiceNum = input("Enter your guess between 1 and 50 ")
        if ranNum == int(choiceNum):
            print("You got it right")
            break
        if ranNum != int(choiceNum):
            input ("That was wrong, you have "+str(2-i)+" guesses left")
        i +=1
    if int(choiceNum) == ranNum:
        print("BRAVO!!! You win")
    if  int(choiceNum) != ranNum:
        print("GAME OVER!!!")

