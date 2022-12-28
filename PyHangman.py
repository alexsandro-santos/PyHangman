import random
from time import sleep
from unidecode import unidecode
from pathlib import Path
from hangman_funcs import clear, display, get_messages

word_lang = {
    "1" : "pt",
    "2" : "en"
    }

clear()
print("\tPyHangman\n\nChoose the language:")
print("1 - Português\n2 - English")
lang_choice = input("Type <1> or <2> and press <Enter>: ")
while lang_choice not in ("1", "2"):
    print("Warning: Invalid option.")
    lang_choice = input("Choose the language: ")

path = Path(f"content/{word_lang[lang_choice]}")

messages = get_messages(path)

with open(path / "words.txt", encoding = "utf-8") as f:
    words = f.read().splitlines()

while True:

    word_number = len(words)
    word = random.choice(words)
    words.remove(word)

    # Fill in the word to be displayed with underscores
    # in place of letters, except for the hyphen.
    displayed_word = ['_' if letter.isalpha() else letter for letter in word]

    wrong_guesses = []  # It stores the incorrect guesses
    mistake_count = 0

    clear() # Clear the screen

    while displayed_word != list(word) and mistake_count < 6:
        print(f"{len(words)}{messages['messages']['word_count']}")
        display(displayed_word, wrong_guesses, mistake_count)
        
        guess = input(f"\n{messages['requests']['guess']}".rstrip('\n')).lower()

        # Error control
        while (
            not guess.isalpha() or
            len(guess) != 1 or
            guess != unidecode(guess)
        ):
            print(f"\n{messages['warnings']['invalid_guess']}")
            guess = input(f"\n{messages['requests']['guess']}".rstrip('\n')).lower()

        if guess in displayed_word:
            print(f"\n{messages['messages']['letter_repeated']}")
        elif guess in unidecode(word):
            for i, letter in enumerate(word):  # Search for the guess in the word
                if unidecode(letter) == guess:  # If the guess is correct,
                    # include the letter in the list in the appropriate position
                    displayed_word[i] = letter
            print(f"\n{messages['messages']['correct_guess']}")
        elif guess in wrong_guesses:  # Increment the mistake counter
            print(f"{messages['messages']['mistake_repeated']}")
            mistake_count += 1
        else:  # Increment the mistake counter
            mistake_count += 1
            wrong_guesses.append(guess)  # Store the incorrect guess
            print(f"\n{messages['messages']['incorrect_guess']}")

        sleep(1)
        clear()

    # Check if the user won or lost
    if mistake_count < 6:
        display(displayed_word, wrong_guesses, mistake_count, messages['messages']['won'])
    else:
        display(
            displayed_word,
            wrong_guesses,
            mistake_count,
            messages['messages']['lost'],
            messages['messages']['show_word'].rstrip('\n') + word
            )

    sleep(2)
    clear()

    while True:
        print (f"{messages['requests']['play_again']}")
        print("\t", end = "")
        r = input().lower()
        if r in ("s", "y", "n"):
            break
        else:
            print(f"{messages['warnings']['invalid_option']}")
    
    if r in ("y", "s"):
        continue
    else:
        break
