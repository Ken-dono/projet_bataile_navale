from Board import Board
from Player import Player
from Submarine import SubMarine

#Variable initialization
is_game_finished = False
is_game_ready = False
Tplayer = [Player(), Player()]
Tboard_display = [Board(), Board()]  # Use for display function
Tboard_sub = [Board(), Board()]
TSub = [SubMarine(), SubMarine()]
count = 0

#Game initialization
while not is_game_ready:
    Tboard_sub[1].place_sub(1, 1, 3, 'e', 1, TSub[1])
    is_game_ready = True


#Play
while not is_game_finished:
    p_index = count % 2
    count += 1
    e_index = count % 2
    print("Player ", p_index + 1, "'s turn")
    Tboard_display[e_index].draw_board()  # Draw the board before choosing coordinate
    x, y, layer = Tplayer[p_index].fire_torpedo(Tboard_sub[e_index])  # Ask and Shoot
    Tboard_display[e_index].clear_info()  # Clear previous shot information
    TSub[e_index].shot_result(x, y, layer, Tboard_sub[e_index], Tboard_display[e_index])# Calculate the result
    #Tboard_display[e_index].draw_board()  # Draw the update board
    # Tboard_sub[e_index].draw_board()

    # FIN DE BOUCLE POUR TEST
    is_game_finished = True
    if is_game_finished:
        break
