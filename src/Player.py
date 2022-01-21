from Board import Board
from Submarine import SubMarine


class Player:
    def __init__(self):
        Board.__init__(self)
        SubMarine.__init__(self)

    def ask_coordinate(self, board):
        valid_layer = False
        while valid_layer == False:
            x = int(input("X : "))
            y = int(input("Y : "))
            layer = int(input("Layer : "))
            if layer == 1 and 0 <= x <= 9 and 0 <= y < 5:
                layer = board.board[layer - 1]
                valid_layer = True
            elif layer == 2 and 0 <= x <= 9 and 0 <= y < 5:
                valid_layer = True
                layer = board.board[layer - 1]
            elif layer == 3 and 0 <= x <= 9 and 0 <= y < 5:
                valid_layer = True
                layer = board.board[layer - 1]
            else:
                print("Invalid coordinates")
        return x, y, layer

    def fire_torpedo(self, board):
        x, y, layer = Player.ask_coordinate(Player, board)
        print("FIRE !!!!!!!")
