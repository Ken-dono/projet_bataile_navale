from Board import Board
from Player import Player
from Submarine import SubMarine

# Variable initialization
is_game_finished = False
is_facing_ok = False
Tplayer = [Player(), Player()]
Tboard_display = [Board(), Board()]  # Use for display function
Tboard_sub = [Board(), Board()]
TSub = [SubMarine(), SubMarine()]
count = 0

# Game initialization
print("-------------GAME INITIALIZATION-------------")
for p_index in range(2):
    print("Player ", p_index + 1, "'s turn")
    Tboard_sub[p_index].draw_board()
    for s_index in range(3):
        print("Submarine n° ", s_index+1, " placement")
        x, y, l = Tplayer[p_index].ask_coordinate(Tboard_sub[p_index])
        facing_list = ["w", "e", "n", "s"]
        f = ""
        while f not in facing_list:
            f = input("Facing (\"w\", \"e\", \"n\", \"s\"): ")
        Tboard_sub[p_index].place_sub(x, y, s_index+1, f, l, TSub[p_index])
    Tboard_sub[p_index].draw_board()
print("-----------------GAME READY------------------")

# Play
while not is_game_finished:
    p_index = count % 2
    count += 1
    e_index = count % 2
    print("Player ", p_index + 1, "'s turn")
    Tboard_display[e_index].draw_board()  # Draw the board before choosing coordinate
    x, y, layer = Tplayer[p_index].fire_torpedo(Tboard_sub[e_index])  # Ask and Shoot
    Tboard_display[e_index].clear_info()  # Clear previous shot information
    result = TSub[e_index].shot_result(x, y, layer, Tboard_sub[e_index], Tboard_display[e_index])  # Calculate the result
    print(result)
    # Tboard_display[e_index].draw_board()  # Draw the update board
    # Tboard_sub[e_index].draw_board()

    # FIN DE BOUCLE POUR TEST
    #is_game_finished = True
    if is_game_finished:
        break
