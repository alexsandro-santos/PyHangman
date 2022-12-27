import os

def clear():

    "Limpa o terminal."

    os.system('cls' if os.name=='nt' else 'clear')

def mistakes(mistakes_number: int):

    "Mostra como está a forca conforme cada erro."

    if mistakes_number == 0:
        print('''
    ______
    |   _|_
    |
    |
    |
    |
    |
    |''')

    elif mistakes_number == 1:
        print('''
    ______
    |   _|_
    |    O
    |
    |
    |
    |
    |''')

    elif mistakes_number == 2:
        print('''
    ______
    |   _|_
    |    O
    |    |
    |
    |
    |
    |''')
    
    elif mistakes_number == 3:
        print('''
    ______
    |   _|_
    |    O
    |   /|
    |
    |
    |
    |''')

    elif mistakes_number == 4:
        print('''
    ______
    |   _|_
    |    O
    |   /|\\
    |
    |
    |
    |''')

    elif mistakes_number == 5:
        print('''
    ______
    |   _|_
    |    O
    |   /|\\
    |   /
    |
    |
    |''')

    elif mistakes_number == 6:
        print('''    /=============\\
    | Você perdeu |
    \\=============/
    ______
    |   _|_
    |    O
    |   /|\\
    |   / \\
    |
    |
    |''')

def win(mistakes_so_far: int):

    "Mostra como estava a forca quando o usuário venceu."

    print('''    /=============\\
    | Você venceu |
    \\=============/''', end = "")
    mistakes(mistakes_so_far)