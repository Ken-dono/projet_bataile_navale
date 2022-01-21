from Board import Board
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
        if player == 1:
            print("Player ", player, "'s turn")
            current_player = player_1
            current_board = board_2
            current_player.fire_torpedo(current_board)
        elif player == 2:
            print("Player ", player, "'s turn")
            current_player = player_2
            current_board = board_1
            current_player.fire_torpedo(current_board)
        if is_game_finished == True:
            break
    player = 1

    #current_board.draw_board()
