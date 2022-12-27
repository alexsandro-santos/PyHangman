import random
from time import sleep
from unidecode import unidecode
from hangman_funcs import clear, mistakes, win

while True:
    with open("words.txt", encoding = "utf-8") as all_words:
        word = random.choice(all_words.readlines()).rstrip()

    secret_word = []

    for letter in word:  # Preenche a lista com "_" equivalente
                         # a quantidade de letras da palavra.
        secret_word.append("_")

    for index, letter in enumerate(word):
        if letter == "-" or letter == " ":
            secret_word[index] = letter

    wrong_attempts = []  # Vai armazenar as letras incorretas
    mistakes_counter = 0  # Contador de erros

    clear() # Limpa a tela

    while secret_word != list(word) and mistakes_counter < 6:
        print("\t", end = "")
        print(*wrong_attempts, sep = " - ") # Imprime as letras incorretas separadas por "-"
        mistakes(mistakes_counter) # Chama a função que imprime a forca
        print("\t", end = "")
        print(*secret_word)  # Imprime os itens da lista separados por um espaço
        attempt = input("\n\tDigite uma letra e pressione <Enter>: ").lower()
        while len(attempt) != 1:  # Controle de erro
            print("\n\tAviso: Somente uma letra por vez!\n")
            attempt = input("\tDigite uma letra e pressione <Enter>: ")
        while attempt != unidecode(attempt):  # Controle de erro
            print("\n\tAviso: Não inclua acentos!\n")
            attempt = input("\tDigite uma letra e pressione <Enter>: ")

        if attempt in secret_word:
            print("\n\tLetra já incluída. Tente outras.")
        elif attempt in unidecode(word):
            for index, letter in enumerate(word):  # Percorre cada letra da palavra
                if unidecode(letter) == attempt:  # Se a letra atual for igual à tentativa do usuário,
                    secret_word[index] = letter   # a letra entra na lista nas posições corretas.
                    
            print("\n\tTentativa correta!")
        elif attempt in wrong_attempts:  # Se a letra já foi digitada, o contador de erros recebe incremento
            print("\tVocê já tentou essa letra antes.")
            mistakes_counter += 1
        else:  # Se a letra for diferente, o contador de erros recebe incremento.
            mistakes_counter += 1
            wrong_attempts.append(attempt) # Coloca as letras incorretas na lista
            print("\n\tTentativa incorreta.")

        sleep(1)
        clear()

    mistakes(mistakes_counter)
    print("\t", end = "")
    print(*secret_word)

    if mistakes_counter < 6:
        clear()
        win(mistakes_counter)
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