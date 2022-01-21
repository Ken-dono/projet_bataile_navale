from Board import Board
from Submarine import SubMarine


class Player:
    def __init__(self):
        Board.__init__(self)

    def ask_coordinate(self, board):
        valid_layer = False
        while not valid_layer:
            x = int(input("X : "))
            y = int(input("Y : "))
            layer = int(input("Layer : "))
            if 0 < layer < 4 and 0 <= y <= 9 and 0 <= x < 5:
                valid_layer = True
            else:
                print("Invalid coordinates")
        return x, y, (layer - 1)

    def fire_torpedo(self, board):
        x, y, layer = Player.ask_coordinate(Player, board)
        print("FIRE !!!!!!!")
        return x,y,layer
