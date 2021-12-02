def is_place_valid(x, y, layer):
	if layer[x][y] != 0 and 0 > x > 9 and 0 > y > 5:
		return False
	else:
		return True


class Board:
	def __init__(self):
		# initialize layers array [y][x]
		self.layer_1 = [['0' for i in range(10)] for j in range(5)]
		self.layer_2 = [['0' for i in range(10)] for j in range(5)]
		self.layer_3 = [['0' for i in range(10)] for j in range(5)]
		self.board = [self.layer_1, self.layer_2, self.layer_3]

	def place_sub(self, x, y, sub, facing, layer):
		for i in range(3):
			if layer == i + 1:
				if sub == 1:
					if is_place_valid(x, y, self.board[i]):
						self.board[i][x][y] = 1
					else:
						print("Erreur case invalide")
				elif sub == 2:
					