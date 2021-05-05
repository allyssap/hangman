# ##hangman python project
import random

# ##a function to select a random word from the list of words in words.txt
def selectWrd():
    with open("words.txt", "r") as file:
        text = file.read()
        words = list(map(str, text.split()))
        return random.choice(words)

def guess():
    print("Please make a guess")
    while(True):
        guess = input()
        # ##check if guess is a valid character -> 41-90 && 61-122
        if(len(guess) > 1):
            print("Invalid Input")
            continue
        if(guess.isalpha()):
            return guess

def newBoard(word, board):
    for letters in word:
        board.append("_")    
    print (*board)

def printBoard(board):
    print (*board)

def checkGuess(word, newGuess, board):
    correct = False
    for i in range(len(word)):
        if(newGuess == word[i]):
            board[i] = newGuess
            correct = True
    
    return correct

def boardFull(board):
    for x in range(len(board)):
        if(board[x] == "_"):
            return False
    return True

def checkLetter(newGuess, letter):
    for letters in letter:
        if(letters == newGuess):
            print("You have already Guessed this letter")
            return False
    letter.append(newGuess)
    return True
        

def main():
    playAgain = True
    print("Welcome to Hangman!")
    while(playAgain):
        # ##These are the letters the player has guessed
        board = []
        letters = []
        word1 = selectWrd()
        word = list(word1)
        newBoard(word, board)
        lives = 0
        while(lives<10):
            ans = False
            while(ans == False):
                newGuess = guess()
                ans = checkLetter(newGuess, letters)

            if(checkGuess(word, newGuess, board) == False):
                print("This letter is not in this word! You lost a try!")
                lives +=1
            printBoard(board)
            if(boardFull(board)):
                print("Congrats you guessed the word ")
                break

        if(lives == 10):
            print("You ran out of tries!")
            print("The word was: ")
        print(word1)
        print("Do you want to play again? y,n")
        if(input() != 'y'):
            playAgain = False
    

if __name__ == "__main__":
    main()