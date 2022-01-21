from Board import Board
<<<<<<< HEAD
from Player import Player

player_1 = Player()
board_1 = Board()
player_2 = Player()
board_2 = Board()
current_player = Player()
current_board = Board()

is_game_finished = False
while is_game_finished == False:
    for player in [1, 2]:
        print("Player ", player, "'s turn")
        if player == 1:
            current_player = player_1
            current_board = board_2
            current_player.fire_torpedo(current_board)
        elif player == 2:
            current_player = player_2
            current_board = board_1
            current_player.fire_torpedo(current_board)
            # FIN DE BOUCLE POUR TEST
            is_game_finished == True
        if is_game_finished == True:
            break
    player = 1

    # current_board.draw_board()
=======
from Submarine import SubMarine

board_p1 = Board()
board_p2 = Board()
Sub_p1 = SubMarine()
board_p1.place_sub(2,2,2,'s',1)
board_p1.draw_board()
Sub_p1.shot_result(2,2,1,board_p1)
Sub_p1.shot_result(2,3,1,board_p1)
board_p1.draw_board()
board_p1.clear_info()
board_p1.draw_board()
>>>>>>> c7bb7b8a769845ca5e484d93d479c0e2b8d7b617
