from Player import Player
from Board import Board
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