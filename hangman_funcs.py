import os

def clear():
    """
    Clear the terminal.
    """

    os.system('cls' if os.name=='nt' else 'clear')

def draw_hangman(mistakes : int):
    """
    Draw the hangman according to the number of mistakes.
    """    
    
    with open('content/base_drawing.txt') as file:
        drawing = file.read()

    body_parts = {
        '1':'0',
        '2':'|',
        '3':'/',
        '4':'\\',
        '5':'/',
        '6':'\\'
    }

    for key, symbol in body_parts.items():
        if int(key) <= mistakes:
            drawing = drawing.replace(key, symbol)
        else:
            drawing = drawing.replace(key, ' ')

    print(drawing)

def display(displayed_word: list, wrong_guesses: list, mistakes: int, message: str = ''):
    print("\t", end = "")
    print(*wrong_guesses, sep = " - ")
    draw_hangman(mistakes)
    print(*displayed_word)
    print(message)
