from Board import Board
from Player import Player
from Submarine import SubMarine


is_game_finished = False
Tplayer = [Player(),Player()]
Tboard = [Board(),Board()]
TSub = [SubMarine(),SubMarine()]
count = 0
while not is_game_finished:
    p_index = count % 2
    count +=1
    e_index = count % 2
    print("Player ", p_index + 1, "'s turn")
    Tboard[p_index].draw_board() #Draw the board before choosing coordinate
    x,y,layer = Tplayer[p_index].fire_torpedo(Tboard[e_index]) #Shoot
    Tboard[p_index].clear_info() #Clear previous shot information
    TSub[p_index].shot_result(x,y,layer,Tboard[p_index]) #Calculate the result
    Tboard[p_index].draw_board() #Draw the update board


    # FIN DE BOUCLE POUR TEST
    is_game_finished = True
    if is_game_finished:
        break
