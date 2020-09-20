#import module
import random

#computer score
compScore = 0
#player score
playerScore = 0
#var por space
x = ''


#Function for user choosing options
def choose():
    #get user choice from input
    userChoice = input("Choose Rock, Paper or Scissors: ")

    #if user types any of the following, convert to correct form...
    if userChoice in ["Rock", "rock", "r", "R"]:
        userChoice = "r"
    elif userChoice in ["Paper", "paper", "p", "P"]:
        userChoice = "p"
    elif userChoice in ["Scissors", "scissors", "s", "S"]:
        userChoice = "s"
    else:
        print("Invalid input. Please try again.")
        choose()
    return userChoice


#Function to generate random computer choice
def computerChoice():
    #assign random integer between 1 and 3
    compChoice = random.randint(1, 3)

    #assing rock, paper or scissor depending on random int
    if compChoice == 1:
        compChoice = "r"
    elif compChoice == 2:
        compChoice = "p"
    else:
        compChoice = "s"
    return compChoice


#make the program run
while True:
    print(x)
    #assign value returned from functions
    userChoice = choose()
    compChoice = computerChoice()
    print(x)

    #if user chooses rock
    if userChoice == "r":
        #tie
        if compChoice == "r":
            print("You: Rock")
            print("Computer: Rock")
            print("Result: Tie!")

        #computer wins
        elif compChoice == "p":
            print("You: Rock")
            print("Computer: Paper")
            print("Result: You lost =(")
            #increase comp score
            compScore += 1

        #user wins
        elif compChoice == "s":
            print("You: Rock")
            print("Computer: Scissors")
            print("You win!!!")
            #increase user score
            playerScore += 1

    #if user chooses paper
    elif userChoice == "p":
        #user wins
        if compChoice == "r":
            print("You: Paper")
            print("Computer: Rock")
            print("Result: You Win!!!")
            #increase user score
            playerScore += 1

        #Tie
        elif compChoice == "p":
            print("You: Paper")
            print("Computer: Paper")
            print("Result: Tie!")

        #computer wins
        elif compChoice == "s":
            print("You: Paper")
            print("Computer: Scissors")
            print("Result: You lost =(")
            #increase comp score
            compScore += 1

    #if user chooses scissors
    elif userChoice == "s":
        #computer wins
        if compChoice == "r":
            print("You: Scissors")
            print("Computer: Rock")
            print("Result: You lost =(")
            #increase comp score
            compScore += 1

        #player wins
        elif compChoice == "p":
            print("You: Scissors")
            print("Computer: Paper")
            print("Result: You win!!!")
            #increase user score
            playerScore += 1

        #Tie
        elif compChoice == "s":
            print("You: Scissors")
            print("Computer: Scissors")
            print("Result: Tie!")

    print(x)
    print("Score: ")
    print("Player: " + str(playerScore))
    print("Computer: " + str(compScore))
    print(x)

    #ask if want to play again
    userChoice = input("Play again? (y/n): ")
    #if yes..
    if userChoice in ["Y", "y", "yes", "Yes"]:
        #continue running program loop
        pass
    elif userChoice in ["N", "n", "no", "No"]:
        #exit loop
        break
    else:
        break
