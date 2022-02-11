# ESEO E3a Angers

import Save
from Board import Board
from Player import Player, is_input_digit
from Submarine import SubMarine
from os import path, name, system, remove

# Variable initialization
is_game_finished = False
is_facing_ok = False
Tplayer = [Player(), Player()]
Tboard_display = [Board(), Board()]  # Use for display function
Tboard_sub = [Board(), Board()]
TSub = [SubMarine(), SubMarine()]
count = 0


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def is_game_finish(sub):
    buffer = 0
    for i in range(3):
        hitnb = len(sub[i][3])
        if hitnb > i + 1:
            hitnb = i + 1
        buffer += hitnb
    if buffer == 6:
        return True
    else:
        return False


choice = 'N'
input_ok = False
while not input_ok:
    choice = input("Load saved game ? (y/N)")
    if choice == 'y' or choice == 'Y' or choice == 'n' or choice == 'N':
        input_ok = True
action = []
is_sub_placed = False
if choice == 'Y' or choice == 'y':
    if path.isfile('./saved_game.thisisnotavirus'):
        action = Save.load_game()
        for i in range(len(action)):
            p_index, e_index, x, y, layer, facing = Save.extract_data(action, i)
            if i < 3:
                print("Player 1 place sub")
                Tboard_sub[p_index].place_sub(x, y, i + 1, facing, layer, TSub[p_index])
            elif i < 6:
                print("Player 2 place sub")
                Tboard_sub[p_index].place_sub(x, y, i - 2, facing, layer, TSub[p_index])
            else:
                TSub[e_index].shot_result(x, y, layer, Tboard_sub[e_index], Tboard_display[e_index])
        is_sub_placed = True
    else:
        print("ERROR NO SAVED GAME")
else:
    if path.isfile('./saved_game.thisisnotavirus'):
        remove("saved_game.thisisnotavirus")

# Game initialization
clear()
if not is_sub_placed:
    print("-------------GAME INITIALIZATION-------------")
    for p_index in range(2):
        print("Player ", p_index + 1, "'s turn")
        Tboard_sub[p_index].draw_board()
        for s_index in range(3):
            sub_ok = False
            while sub_ok == False:
                print("Submarine n° ", s_index + 1, " placement")
                x = is_input_digit(input("X : "))
                y = is_input_digit(input("Y : "))
                l = is_input_digit(input("Layer : "))
                f = input("Facing (\"w\", \"e\", \"n\", \"s\"): ")
                facing_list = ["w", "e", "n", "s"]
                if 0 < l < 4 and 0 <= y <= 9 and 0 <= x <= 4 and f in facing_list:
                    sub_ok = Tboard_sub[p_index].place_sub(x, y, s_index + 1, f, l-1, TSub[p_index])
                else:
                    print("Invalid coordinates")
            Save.record_action(p_index, x, y, l, f)
        print("")
        print("Player ", p_index + 1, "'s board")
        Tboard_sub[p_index].draw_board()
        input("Appuyer sur une touche pour passer au joueur suivant")
        clear()
    print("-----------------GAME READY------------------")

# Play
while not is_game_finished:
    clear()
    p_index = count % 2
    count += 1
    e_index = count % 2
    facing = 'x'  # Default value when not placing sub
    print("Player ", p_index + 1, "'s turn")
    Tboard_display[e_index].draw_board()  # Draw the board before choosing coordinate
    x, y, layer = Tplayer[p_index].fire_torpedo(Tboard_sub[e_index])  # Shoot
    Tboard_display[e_index].clear_info()  # Clear previous shot information
    # Calculate the result
    TSub[e_index].shot_result(x, y, layer, Tboard_sub[e_index], Tboard_display[e_index])

    Tboard_display[e_index].draw_board()  # Draw the update board

    # FIN DE BOUCLE POUR TEST
    Save.record_action(p_index, x, y, layer, facing)
    is_game_finished = is_game_finish(TSub[e_index].sub)
    if is_game_finished == True:
        print(r"""
        ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗    ██╗██╗
        ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║    ██║██║
        ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║    ██║██║
        ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║    ╚═╝╚═╝
        ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗██╗
        ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝╚═╝                     
                            """)
        break
    input("Appuyer sur une touche pour passer au joueur suivant")
