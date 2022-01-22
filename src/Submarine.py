from Board import Board


def is_sub_here(x, y, layer, board):
    if board.board[layer][x][y] == 'S':
        return True
    else:
        return False


def is_sub_around(x, y, layer, board_sub, board_display):
    see = False
    for i in range(y - 1, y + 2, 1):
        if not see and 10 > i >= 0:
            if is_sub_here(x, i, layer, board_sub):
                see = True
    if not see:
        for v in range(x - 1, x + 2, 1):
            if not see and 5 > v >= 0:
                if is_sub_here(v, y, layer, board_sub):
                    see = True
    if see:
        for i in range(y - 1, y + 2, 1):
            if 10 > i >= 0:
                if board_display.board[layer][x][i] != 'T':
                    board_display.board[layer][x][i] = 'V'
        for v in range(x - 1, x + 2, 1):
            if 5 > v >= 0:
                if board_display.board[layer][v][y] != 'T':
                    board_display.board[layer][v][y] = 'V'
        return True
    else:
        return False


def no_one_around(x, y, layer, board):
    for i in range(y - 1, y + 2, 1):
        if 10 > i >= 0:
            if board.board[layer][x][i] != 'T':
                board.board[layer][x][i] = 'R'
    for v in range(x - 1, x + 2, 1):
        if 5 > v >= 0:
            if board.board[layer][v][y] != 'T':
                board.board[layer][v][y] = 'R'


class SubMarine:
    sub_1 = None
    sub_2 = None
    sub_3 = None

    def __init__(self):
        self.sub_1 = [[], [], []]  # [[layer],[x],[y]]
        self.sub_2 = [[], [], []]  # [[layer],[x,x],[y,y]]
        self.sub_3 = [[], [], []]  # [[layer],[x,x,x],[y,y,y]]
        self.sub = [self.sub_1, self.sub_2, self.sub_3]

    def shot_result(self, x, y, layer, board_sub, board_display):
        if is_sub_here(x, y, layer, board_sub):
            # board.board[layer][x][y] = 'T'
            SubMarine.damage_sub(self, x, y, layer, board_display)
        else:
            if is_sub_around(x, y, layer, board_sub, board_display):
                return 1
            else:
                no_one_around(x, y, layer, board_display)

    def damage_sub(self, x, y, layer, board):
        save_index = 0
        for i in range(3):  # Check all Sub
            # Find Subs in the right layer
            if len(self.sub[i][1]) > 0 and self.sub[i][0][0] == layer:
                for v in range(len(self.sub[i][1])):
                    if self.sub[i][1][v] == x and self.sub[i][2][v] == y:
                        # Find the right Sub
                        save_index = v  # Save the index in the list
                        break
                self.sub[i][1].pop(save_index)  # Delete the coordinate
                self.sub[i][2].pop(save_index)
        board.board[layer][x][y] = 'T'
