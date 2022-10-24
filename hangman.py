# Write your code here
import random

print("H A N G M A N\n")

games_won = 0
attempts = 8
games_lost = 0

# print("".join(letters) + " " + "".join(letters_hashed))
def hangman():
    global attempts
    global games_won
    global games_lost
    words = ['python', 'java', 'swift', 'javascript']
    word = random.choice(words)
    word = list(word)
    guesses = list()
    hashed_word = list("-" * len(word))
    print("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")
    option = input()
    if option == "play":
        attempts = 8
        while attempts > 0:
            print("".join(hashed_word))
            print("Input a letter:")
            letter = input()
            if len(letter) != 1:
                print("Please, input a single letter.")
                continue
            if letter < 'a' or letter > 'z':
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            if letter in guesses:
                print("You've already guessed this letter.")
                continue
            guesses.append(letter)
            if letter not in word:
                attempts -= 1
                print("That letter doesn't appear in the word.")
            else:
                if letter not in hashed_word:
                    for i in range(len(word)):
                        if word[i] == letter:
                            hashed_word[i] = letter
                    if '-' not in hashed_word:
                        print("You guessed the word " + "".join(hashed_word) + "!")
                        games_won += 1
                        break
                else:
                    print("No improvements.")
                    attempts -= 1
        if attempts == 0:
            games_lost += 1
            print("You lost!")
        else:
            print("You survived!")
        hangman()
    elif option == "results":
        print("You won: " + str(games_won) + " times")
        print("You lost: " + str(games_lost) + " times")
        hangman()
    else:
        return

hangman()
