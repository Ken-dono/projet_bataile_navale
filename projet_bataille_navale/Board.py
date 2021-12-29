def is_place_valid(x, y, layer):
    if layer[x][y] == 0 and 0 > x > 9 and 0 > y > 5:
        return True
    else:
        return False


def facing_coordinates(x, y, facing, size):
    x2 = x
    y2 = y
    x3 = x
    y3 = y
    if facing == 's':
        y2 += 1
        y3 += 2
    elif facing == 'n':
        y2 -= 1
        y3 -= 2
    elif facing == 'w':
        x2 -= 1
        x3 -= 2
    elif facing == 'e':
        x2 += 1
        x3 += 2
    if size == 2:
        return x2, y2  # return only needed coordinate
    elif size == 3:
        return x2, y2, x3, y3  # return only needed coordinate


class Board:
    def __init__(self):
        # initialize layers array [y][x]
        self.layer_1 = [['0' for i in range(10)] for j in range(5)]
        self.layer_2 = [['0' for i in range(10)] for j in range(5)]
        self.layer_3 = [['0' for i in range(10)] for j in range(5)]
        self.board = [self.layer_1, self.layer_2, self.layer_3]

    def place_sub(self, x, y, sub, facing, layer):
        if 0 > layer or layer > 2:
            return -1
        if sub == 1:
            if is_place_valid(x, y, self.board[layer]):
                self.board[layer][x][y] = 1
            else:
                print("Erreur case invalide")
        elif sub == 2:
            x2, y2 = facing_coordinates(x, y, facing, sub)
            if is_place_valid(x, y, self.board[layer]) and \
                    is_place_valid(x2, y2, self.board[layer]):
                self.board[layer][x][y] = 1
                self.board[layer][x2][y2] = 1
            else:
                print("Erreur case invalide")
        elif sub == 3:
            x2, y2, x3, y3 = facing_coordinates(x, y, facing, sub)
            if is_place_valid(x, y, self.board[layer]) and \
                    is_place_valid(x2, y2, self.board[layer]) and \
                    is_place_valid(x3, y3, self.board[layer]):
                self.board[layer][x][y] = 1
                self.board[layer][x2][y2] = 1
                self.board[layer][x3][y3] = 1
            else:
                print("Erreur case invalide")
