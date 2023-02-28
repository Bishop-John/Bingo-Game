import random
allNumbers = []
usedNumbers = []

for i in range(1,91):
    allNumbers.append(i)

for i in range(90):
    currentNumber = random.choice(allNumbers)
    print (currentNumber)
    allNumbers.remove(currentNumber)
    usedNumbers.append(currentNumber)
    winnerYet = input("Has anybody won... ")
    if winnerYet == "y":
        print ("We may have a winner!")
        print ("Here are the called numbers so far... ")
        usedNumbers.sort()# Put the numbers in order for easy reading
        print (usedNumbers)
        reallyWon = input("Did the player really win?")
        if reallyWon == "y":
            print ("WINNER!!!")
            break
        else:
            ("That was not a winning ticket. Game contines...")
