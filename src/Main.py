import Save
from Board import Board
from Player import Player
from Submarine import SubMarine

is_game_finished = False
Tplayer = [Player(), Player()]
Tboard_display = [Board(), Board()]  # Use for display function
Tboard_sub = [Board(), Board()]
TSub = [SubMarine(), SubMarine()]
count = 0
Tboard_sub[1].place_sub(1, 1, 1, 'e', 1, TSub[1])


def is_game_finish(self, sub):
    buffer = 0
    for _ in range(3):
        buffer += len(sub[_][3])
    return buffer == 6


choice = 'N'
input_ok = False
while not input_ok:
    choice = input("Load saved game ? (y/N)")
    if choice == 'y' or choice == 'Y' or choice == 'n' or choice == 'N':
        input_ok = True
action = []
if choice == 'Y' or choice == 'y':
    action = Save.load_game()
    for i in range(len(action)):
        p_index, e_index, x, y, layer, facing = Save.extract_data(action, i)
        if i < 3:
            Tboard_sub[p_index].place_sub(x, y, i, facing, layer, TSub[p_index])
        elif i < 6:
            Tboard_sub[p_index].place_sub(x, y, i, facing, layer, TSub[p_index])
        else:
            TSub[e_index].shot_result(x, y, layer, Tboard_sub[e_index], Tboard_display[e_index])

while not is_game_finished:
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
    # is_game_finished = True
    # if is_game_finished:
    #     break
