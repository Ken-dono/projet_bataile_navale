from Board import Board
from Player import Player

board_1 = Board()
player_1 = Player()

is_game_finished = False
while is_game_finished == False:
    player_1.fire_torpedo(board_1)
    is_game_finished = True
# board.draw_board()
