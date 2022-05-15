"""
EN: This is my first Python Game. It is a simple Jokenpo game. And you can use cheats on it. Thats all, enjoy!
PT: Este é o meu primeito jogo em Python. É um simples pedra-papel-tesoura. E temos cheats! Divirta-se.
"""

from random import randint
from JoKenPo_DATA import *


##########################################################################################################
# Functions begins here

def playing_game():
    """
    Objective: main game function. Manage all game inputs and call the appropriate functions.
    :return:
    """
    cheat = False
    print(BEGIN_PLAYING_TEXT[language])

    while True:

        computer = computer_move(cheat)     # Computer makes its move
        move = input().lower()              # Player makes its move

        if move in inputs:

            if inputs[move] == "cheat":
                cheat = cheating(cheat)

            elif not inputs[move]:  # "exit" = False
                return

            else:
                player = inputs[move]
                game_round(player, computer)
                print(NEW_TURN[language])

        else:
            print(USER_TYPED_IT_WRONG[language] + WRONG_WHILE_PLAYING[language])


def game_round(player, computer):

    print(name + MOVE[language] + MOVES[language][player - 1])
    print(pc_name + MOVE[language] + MOVES[language][computer - 1])

    if VICTORY_MATRIX[player - 1][computer - 1] == 0:
        print(DRAW[language])

    elif VICTORY_MATRIX[player - 1][computer - 1] == 1:
        print(name + WON[language] + " " + pc_name + LOSE[language])

    else:
        print(pc_name + WON[language] + " " + name + LOSE[language])

    return


def computer_move(cheat):

    computer = randint(1, 3)

    if cheat:
        print(PC_MOVE_4_XITERS[language] + MOVES[language][computer - 1])  # Showing PC move for cheaters

    return computer


def cheating(cheat_state):
    cheat_state = not cheat_state
    print(IM_A_XITER[language]) if cheat_state else print(NO_MORE_XITER[language])

    return cheat_state

# Functions ends here
##########################################################################################################


# MAIN
print("Select your language (type EN)\nSelecione o teu idioma (digite PT)")

while True:
    language = input().upper()
    if language in ("EN", "PT"):
        break
    print("Please, type a valid language (EN or PT).\nPor favor, digite um idioma válido (EN ou PT).")

if language == "EN":
    inputs = INPUT_EN
    init_inputs = INIT_INPUT_EN
    language = 0
    print("Now, type your name:")
    name = input()
    print("And finally, a name for your opponent:")
    pc_name = input()

elif language == "PT":
    inputs = INPUT_PT
    init_inputs = INIT_INPUT_PT
    language = 1
    print("Agora, digita o teu nome:")
    name = input()
    print("E por fim, um nome para o teu rival:")
    pc_name = input()

else:
    inputs = {}
    init_inputs = {}
    language = -1
    name = "DarkCyborg"
    pc_name = "Homura Akemi"


print(WELCOME_TEXT[language])

while True:
    if language == -1:      # If there was any mistake in language setting
        print(ERROR[0])
        print(ERROR[1])
        raise ValueError("No language found.")

    current_input = input().lower()

    if current_input in init_inputs:
        if init_inputs[current_input]:   # current_input == play: true
            playing_game()
            print(BACK_TO_TITLE_TEXT[language])
        else:                            # current_input == exit: false
            break
    else:                                # user typed something wrong
        print(USER_TYPED_IT_WRONG[language] + WRONG_IN_MAIN_SCREEN[language])

