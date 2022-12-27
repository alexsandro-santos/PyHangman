import random
from time import sleep
from unidecode import unidecode
from hangman_funcs import clear, mistakes, win

with open('words.txt', encoding = "utf-8") as f:
        words = f.read().splitlines()

while True:

    word_number = len(words)
    word = random.choice(words)
    words.remove(word)

    # Fill in the word to be displayed with underscores
    # in place of letters, except for the hyphen.
    displayed_word = ['_' if letter != '-' else letter for letter in word]

    wrong_guesses = []  # It stores the incorrect guesses
    mistake_count = 0

    clear() # Clear the screen

    print(f"{len(words)} more words available to play.")

    while displayed_word != list(word) and mistake_count < 6:
        print("\t", end = "")
        print(*wrong_guesses, sep = " - ") # Display the wrong letters guessed
        mistakes(mistake_count) # Print the updated hangman
        print("\t", end = "")
        # Display the correct guesses in the correct place in the word
        print(*displayed_word) 
        
        guess = input("\n\tType a letter and press <Enter>: ").lower()

        # Error control
        while (
            not guess.isalpha() or
            len(guess) != 1 or
            guess != unidecode(guess)
        ):
            print("\n\twarning: Invalid guess!")
            print("\tDo not use more than one letter at a time.")
            print("\tDo not use accents.\n")
            guess = input("\tType a letter and press <Enter>: ")

        if guess in displayed_word:
            print("\n\tLetter already included. Make another guess.")
        elif guess in unidecode(word):
            for i, letter in enumerate(word):  # Search for the guess in the word
                if unidecode(letter) == guess:  # If the guess is correct,
                    # include the letter in the list in the appropriate position
                    displayed_word[i] = letter
            print("\n\tCorrect guess!")
        elif guess in wrong_guesses:  # Increment the mistake counter
            print("\tYou've tried that letter before.")
            mistake_count += 1
        else:  # Increment the mistake counter
            mistake_count += 1
            wrong_guesses.append(guess)  # Store the incorrect guess
            print("\n\tIncorrect guess.")

        sleep(1)
        clear()

    mistakes(mistake_count)
    print("\t", end = "")
    print(*displayed_word)

    if mistake_count < 6:
        clear()
        win(mistake_count)
    else:
        print("\n\tThe word was '" + word + "'.\n")
    sleep(2)
    clear()

    while True:
        print ("\tWould you like to keep playing? Type <Y> or <N> and press <Enter>.")
        print("\t", end = "")
        r = input().lower()
        if r in ("s", "y", "n"):
            break
        else:
            print("\tWarning: Invalid option.")
    
    if r in ("y", "s"):
        continue
    else:
        break