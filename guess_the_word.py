import random

#global variables

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

word_tuple = ("cat", "dog", "duck", "aardvark",
              "elephant", "giraffe", "zebra")
secret_word = random.choice(word_tuple)

leaderboard = {}
moves = 0
blank_word = []


def start_screen():
    print("======================================")
    print("Welcome to GUESS THE WORD GAME!")
    print("You will be given a number of dashes equivalent to the number of letters in the word.")
    print("You will guess a letter that goes in the secret word.")
    print("If you get 6 wrong guesses, you lose the game!")
    print("=======================================")


def present_blank_word():
    for letter in secret_word:
        blank_word.append("___")
    print(blank_word)


def guess_word():
    global moves
    global username
    wrong_guess = 0

    while wrong_guess < 6:
        guess = input("Guess a letter or type the full word: ")
        guess = guess.lower()
      # if guess is one letter or the full word
        if len(guess) == 1 or len(guess) == len(secret_word):
            if guess == secret_word:
                print("You guessed the word!!")
                print("Congratulations!! You won!!!")
                if username not in leaderboard or len(leaderboard) == 0 or leaderboard[username] > moves:
                    leaderboard.update({username: moves})
                print("Current leaderboard score: ")
                print(leaderboard)
                break
            else:
                if guess in secret_word:
                    print("You guessed right!")
                    alphabet.remove(guess)
                    for letter in range(len(secret_word)):
                        if guess == secret_word[letter]:
                            blank_word[letter] = secret_word[letter]
                    print(blank_word)
                    moves += 1
                    print("Current number of moves:", moves)

                    if "___" not in blank_word:
                        print("Congratulations!! You won!!!")
                        leaderboard.update({username: moves})
                        print("Current leaderboard score: ")
                        print(leaderboard)
                        break
                else:
                    print("You guessed wrong.")
                    moves += 1
                    wrong_guess += 1
                    print("Number of wrong guesses:", wrong_guess)
        else:
            print("Please type in one letter or the full word.")
            moves += 1
            print("Current moves:", moves)


start_screen()
leaderboard = {}

while True:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    word_tuple = ("cat", "dog", "duck", "aardvark",
                  "elephant", "giraffe", "zebra")
    secret_word = random.choice(word_tuple)

    moves = 0
    blank_word = []
    play = input("Would you like to play the game? Press Y or N")
    if play.lower() == "n":
        print("Goodbye.")
        break
    else:
        global username
        username = input("Enter your name: ")

        present_blank_word()
        guess_word()
