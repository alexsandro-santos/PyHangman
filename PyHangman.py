import random
from time import sleep
from unidecode import unidecode
from hangman_funcs import clear, mistakes, win

while True:
    with open("words.txt", encoding = "utf-8") as all_words:
        word = random.choice(all_words.readlines()).rstrip()

    # Fill in the word to be displayed with underscores
    # in place of letters, except for the hyphen.
    displayed_word = ['_' if letter != '-' else letter for letter in word]

    wrong_guesses = []  # Store the wrong letters guessed
    mistake_count = 0

    clear() # Clear the screen

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
            not guess.isalpha() and
            len(guess) != 1 and
            guess != unidecode(guess)
        ):
            print("\n\twarning: Invalid guess!")
            print("\tDo not use more the one letter at a time.")
            print("\tDo not use accents.\n")
            guess = input("\tType a letter and press <Enter>: ")

        if guess in displayed_word:
            print("\n\tLetter already included. Make another guess.")
        elif guess in unidecode(word):
            for i, letter in enumerate(word):  # Search for the guess in the word
                if unidecode(letter) == guess:  # If the guess is correct,
                    # the letter is included in the list in the correct position
                    displayed_word[i] = letter
            print("\n\tTentativa correta!")
        elif guess in wrong_guesses:  # Se a letra já foi digitada, o contador de erros recebe incremento
            print("\tVocê já tentou essa letra antes.")
            mistake_count += 1
        else:  # Se a letra for diferente, o contador de erros recebe incremento.
            mistake_count += 1
            wrong_guesses.append(guess) # Coloca as letras incorretas na lista
            print("\n\tTentativa incorreta.")

        sleep(1)
        clear()

    mistakes(mistake_count)
    print("\t", end = "")
    print(*displayed_word)

    if mistake_count < 6:
        clear()
        win(mistake_count)
    else:
        print("\n\tA palavra era '" + word + "'.\n")
    sleep(2)
    clear()

    while True:
        print ("\tDeseja continuar jogando? Digite <S> ou <N> e tecle <Enter>.")
        print("\t", end = "")
        r = input().lower()
        if r == "s" or r == "n":
            break
        else:
            print("\tOpção inválida.")
    
    if r == "s":
        continue
    else:
        break