from random import sample

class Minesmap:
	def __init__(self, width, height, number_of_mines):
		self.height = height
		self.width = width
		seed = sample(range(width * height), number_of_mines)
		minesmap = [[0 for j in range(height)] for i in range(width)]
		for num in seed:
			minesmap[num//height][num%height] = 1
		self._minesmap = tuple(tuple(sublist) for sublist in minesmap)
		self._revived = [[0 for j in range(height)] for i in range(width)]
		self._flag = [[0 for j in range(height)] for i in range(width)]

	def around(self, x, y):
		return [(i, j) for j in range(max(0, y - 1),min(self.height, y + 2)) for i in range(max(0, x - 1),min(self.width, x + 2))]

	def getnumber(self, x, y):
		around = 0
		for i, j in self.around(x, y):
			if self._minesmap[i][j]:
				around += 1
		return around

	def revive(self, x, y):
		self._revived[x][y] = 1
		if self._minesmap[x][y]:
			return True
		if self.getnumber(x, y):
			return False
		else:
			for i, j in self.around(x, y):
				if not self._revived[i][j]:
					Minesmap.revive(self, i, j)
			return False

	def setflag(self, x, y):
		self._flag[x][y] = 1

	def flagrevive(self, x, y):
		for i, j in self.around(x, y):
			if not self._flag[i][j]:
				self.revive[i][j]

	def outer(self):
		for i in range(self.width):
			for j in range(self.height):
				print(("*" if self._minesmap[i][j] else self.getnumber(i, j)) if self._revived[i][j] else '+', end='')	
			print()

	def inner(self):
		for i in range(self.width):
			for j in range(self.height):
				print(1 if self._minesmap[i][j] else 0, end='')
			print()