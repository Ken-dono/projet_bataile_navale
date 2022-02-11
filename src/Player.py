from Board import Board
from Submarine import SubMarine

def is_input_digit(input):
    if input.isdigit():
        return int(input)
    else:
        return -1
class Player:
    def __init__(self):
        Board.__init__(self)

    def ask_coordinate(self, board):
        valid_layer = False
        while not valid_layer:
            x = is_input_digit(input("X : "))
            y = is_input_digit(input("Y : "))
            layer = is_input_digit(input("Layer : "))
            if 0 < layer < 4 and 0 <= y <= 9 and 0 <= x <= 4:
                valid_layer = True
            else:
                print("Invalid coordinates")
        return x, y, (layer - 1)

    def fire_torpedo(self, board):
        x, y, layer = Player.ask_coordinate(Player, board)
        print(r"""
        ███████╗██╗██████╗ ███████╗    ██╗██╗██╗
        ██╔════╝██║██╔══██╗██╔════╝    ██║██║██║
        █████╗  ██║██████╔╝█████╗      ██║██║██║
        ██╔══╝  ██║██╔══██╗██╔══╝      ╚═╝╚═╝╚═╝
        ██║     ██║██║  ██║███████╗    ██╗██╗██╗
        ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝╚═╝╚═╝                      
                    """)
        return x,y,layer
