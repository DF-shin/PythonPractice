# Magic 8 Ball
import random

ballResponses = ["You look ugly", "Come back tomorrow", "Can't you see I'm working?", "You win dumbass of the year!", "I'd wine an' dine ya", 
                "Stupid idiot can't count", "Screw off", "My favourite song is by Will Smith"]

ballPrediction = ballResponses[random.randint(0, len(ballResponses)-1)]

userInput2 = input("Ask me anything: ")
print(ballPrediction)

while True:
    ballPrediction = ballResponses[random.randint(0, len(ballResponses)-1)]
    userInput2 = input("Wanna ask something else? YES:NO  ")

    if userInput2.capitalize() == "Yes" or userInput2.capitalize() == "Y":
        userInput2 = input("Ask me something else: ")
        print(ballPrediction)
    elif userInput2.capitalize() == "No" or userInput2.capitalize() == "N":
        break
    else:
        print("Not a response")


print("See you later!")