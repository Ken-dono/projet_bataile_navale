from Board import Board

def is_sub_here(x,y,layer, board):
	print(x,y,layer)
	if board.board[layer][x][y] == '1':
		return True
	else:
		return False

def is_sub_around(x,y,layer,board):
	see = False
	for i in range(y - 1, y + 2, 1):
		if not see and 10 > i >= 0:
			if is_sub_here(x, i, layer, board):
				see = True
	if not see:
		for v in range(x - 1, x + 2, 1):
			if not see and 5 > x >= 0:
				if is_sub_here(v, y, layer, board):
					see = True
	if see:
		for i in range(y - 1, y + 2, 1):
			if 10 > x >= 0:
				if board.board[layer][x][i] != 'T':
					board.board[layer][x][i] = 'V'
		for v in range(x - 1, x + 2, 1):
			if 5 > y >= 0:
				if board.board[layer][v][y] != 'T':
					board.board[layer][v][y] = 'V'
		return True
	else:
		return False

def no_one_around(x,y,layer,board):
	for i in range(y - 1, y + 2, 1):
		if 10 > y >= 0:
			if board.board[layer][x][i] != 'T':
				board.board[layer][x][i] = 'R'
	for v in range(x - 1, x + 2, 1):
		if 5 > x >= 0:
			if board.board[layer][v][y] != 'T':
				board.board[layer][v][y] = 'R'

class SubMarine:
	sub_1 = None
	sub_2 = None
	sub_3 = None

	def __init__(self):
		self.sub_1 = []
		self.sub_2 = []
		self.sub_3 = []

	def shot_result(self,x,y,layer, board):
		if is_sub_here(x,y,layer,board):
			board.board[layer][x][y] = 'T'
		else:
			if is_sub_around(x,y,layer,board):
				return 1
			else:
				no_one_around(x,y,layer,board)

