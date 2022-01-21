from Board import Board
from Player import Player
from Submarine import SubMarine

player_1 = Player()
board_1 = Board()
sub_1 = SubMarine()
player_2 = Player()
board_2 = Board()
sub_2 = SubMarine()
current_player = Player()
current_board = Board()
current_sub = SubMarine()
is_game_finished = False
while not is_game_finished:
    for player in [1, 2]:
        print("Player ", player, "'s turn")
        if player == 1:
            current_player = player_1
            current_board = board_2
            current_sub = sub_2
            x,y,layer = current_player.fire_torpedo(current_board)
            current_sub.shot_result(x, y, layer, current_board)
            current_board.draw_board()
        elif player == 2:
            current_player = player_2
            current_board = board_1
            current_sub = sub_1
            current_player.fire_torpedo(current_board)
            current_board.draw_board()
            # FIN DE BOUCLE POUR TEST
            # is_game_finished = True
        if is_game_finished:
            break
    player = 1

    # current_board.draw_board()
