import os
from pathlib import Path

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

def display(displayed_word: list, wrong_guesses: list, mistakes: int, *messages):
    """
    Show game display updated.
    """
    print("\t", end = "")
    print(*wrong_guesses, sep = " - ")
    draw_hangman(mistakes)
    print("\t", end = "")
    print(*displayed_word)
    for message in messages:
        print(message)

def get_messages(path: Path) -> dict:
    """
    Get the game messages for a specific language.
    """
    with open(path / "game_text.txt", encoding = "utf-8") as file:
        in_category = False
        in_message = False
        messages = dict()
        
        for line in file:
            if not in_category:
                if line.strip() == "":
                    continue
                else:
                    category = line.strip('{}\n')
                    messages[category] = dict()
                    in_category = True
            elif in_category:
                if line.strip('{}\n') == category:
                    in_category = False
                elif not in_message:
                    msg_key = line.strip('[]\n')
                    messages[category.strip('{}\n')][msg_key] = str()
                    in_message = True
                elif in_message and line.strip('[]\n') == msg_key:
                    in_message = False
                elif in_message:
                    messages[category.strip('{}\n')][msg_key.strip('[]\n')] += line
    
    return messages
