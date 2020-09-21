import random
from words import wordList


def getWord():
    #get random word from list file
    word = random.choice(wordList)
    #return it in upper case for comparison
    return word.upper()


#function to play game passing word to be guessed
def play(word):
    #vars for game
    wordToGuess = "_" * len(word)
    guessed = False  #word/guess status
    #lists for player guessed letters and words
    guessedLetters = []
    guessedWords = []
    #how many tries (parts of body to be drawn)
    tries = 6

    #interface
    print("Let's start the game!")
    print(displayGame(tries))
    print(wordToGuess)
    print("\n")

    #play until word is guessed or tries run out
    while not guessed and tries > 0:
        #store guess from input
        guess = input("Please enter a letter or word: ").upper()

        #validate that input letter is alpha and was entered
        if len(guess) == 1 and guess.isalpha():
            #if player already tried that letter...
            if guess in guessedLetters:
                print("You already tried:", guess)
            #if letter is not in the word to be guessed
            elif guess not in word:
                print(guess, "is not in the word.")
                #decrease tries left
                tries -= 1
                #add the guess to list of letters already guessed
                guessedLetters.append(guess)
            #if letter is in the word
            else:
                print("Good job,", guess, "is in the word!")
                #add to letters already guessed
                guessedLetters.append(guess)
                #convert string to list to index it
                wordList = list(wordToGuess)
                #use list comprehension
                #if guess is equal to letter append it to word to be guessed
                indices = [
                    i for i, letter in enumerate(word) if letter == guess
                ]
                #loop through indices
                for index in indices:
                    #replace with guess
                    wordList[index] = guess
                #rejoin as string and update var
                wordToGuess = "".join(wordList)
                #if letter entirely guessed...
                if "_" not in wordToGuess:
                    guessed = True

#validate that input word is equal to word from game and is alpha
        elif len(guess) == len(word) and guess.isalpha():
            #check if correct
            if guess in guessedWords:
                print("You already guessed the whole word", guess)
            elif guess != word:
                print(guess, "is not the word. Try again!")
                #decrease tries
                tries -= 1
                #append to words already guessed
                guessedWords.append(guess)
            else:
                #guessed correctly
                guessed = True
                #fill the word
                wordToGuess = word

        #not alpha, not word, not letter..
        else:
            print("Not a valid guess.")

#continue to try
        print(displayGame(tries))
        print(wordToGuess)
        print("\n")

        #congratualte or say sorry
    if guessed:
        print("Congrats. You win!")
    else:
        print("Sorry, bad luck. The word was " + word + "!")


#functon to display game
def displayGame(tries):
    #list of stages related to number of tries left
    stages = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """, """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """, """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """, """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """, """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """, """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """, """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    #get the word
    word = getWord()
    #play with the word
    play(word)

    #keep playing while user wants to play
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = getWord()
        play(word)


#in order to run on commandline
if __name__ == "__main__":
    main()