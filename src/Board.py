def is_place_valid(x, y, layer):
    if layer[x][y] == '_' and 4 >= x >= 0 and 9 >= y >= 0:
        return True
    else:
        return False


def facing_coordinates(x, y, facing, size):
    x2 = x
    y2 = y
    x3 = x
    y3 = y
    if facing == 'e':
        y2 += 1
        y3 += 2
    elif facing == 'w':
        y2 -= 1
        y3 -= 2
    elif facing == 'n':
        x2 -= 1
        x3 -= 2

    elif facing == 's':
        x2 += 1
        x3 += 2
    if size == 2:
        return x2, y2  # return only needed coordinate
    elif size == 3:
        return x2, y2, x3, y3  # return only needed coordinate


class Board:
    def __init__(self):
        # initialize layers array [y][x]
        self.layer_1 = [['_' for i in range(10)] for j in range(5)]
        self.layer_2 = [['_' for i in range(10)] for j in range(5)]
        self.layer_3 = [['_' for i in range(10)] for j in range(5)]
        self.board = [self.layer_1, self.layer_2, self.layer_3]

    def place_sub(self, x, y, sub, facing, layer, submarine):
        if 0 > layer or layer > 2:
            return -1
        if sub == 1:
            if is_place_valid(x, y, self.board[layer]):
                self.board[layer][x][y] = 'S'
                submarine.sub[0][0].append(layer)
                submarine.sub[0][1].append(x)
                submarine.sub[0][2].append(y)
            else:
                print("Erreur case invalide")
        elif sub == 2:
            x2, y2 = facing_coordinates(x, y, facing, sub)
            if is_place_valid(x, y, self.board[layer]) and \
                    is_place_valid(x2, y2, self.board[layer]):
                submarine.sub[1][0].append(layer)
                submarine.sub[1][1].append(x)
                submarine.sub[1][1].append(x2)
                submarine.sub[1][2].append(y)
                submarine.sub[1][2].append(y2)
                self.board[layer][x][y] = 'S'
                self.board[layer][x2][y2] = 'S'
            else:
                print("Erreur case invalide")
        elif sub == 3:
            x2, y2, x3, y3 = facing_coordinates(x, y, facing, sub)
            if is_place_valid(x, y, self.board[layer]) and \
                    is_place_valid(x2, y2, self.board[layer]) and \
                    is_place_valid(x3, y3, self.board[layer]):
                print("")
                submarine.sub[2][0].append(layer)
                submarine.sub[2][1].append(x)
                submarine.sub[2][1].append(x2)
                submarine.sub[2][1].append(x3)
                submarine.sub[2][2].append(y)
                submarine.sub[2][2].append(y2)
                submarine.sub[2][2].append(y3)
                self.board[layer][x][y] = 'S'
                self.board[layer][x2][y2] = 'S'
                self.board[layer][x3][y3] = 'S'
            else:
                print("Erreur case invalide")

    def draw_board(self):
        legend = [str(i) for i in range(10)]
        for i in range(3):
            print("Couche :",str(i + 1)+"00 mètres")
            print("   ", end='')
            for y in range(10):
                print("  " + legend[y] + "  ", end='')
            print('')

            for v in range(5):
                print(v, end="  ")
                print(self.board[i][v])

    def clear_info(self):
        for i in range(3):
            for v in range(5):
                for y in range(10):
                    # print(i,v,y)
                    if self.board[i][v][y] == 'V' or \
                            self.board[i][v][y] == 'R':
                        self.board[i][v][y] = '_'
