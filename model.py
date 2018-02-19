from random import sample

class Block:
	def __init__(self):
		self._mine = False
		self._revived = False
		self._flaged = False
		self._rounding = 0
	def getmine(self):
		return self._mine
	def setmine(self):
		self._mine = True
	def getrounding(self):
		return self._rounding
	def setrounding(self, num):
		self._rounding = num
	def getflag(self):
		return self._flaged
	def setflag(self):
		self._flaged = not self._flaged
	def revived(self):
		return self._revived
	def revive(self):
		self._revived = True

class Minesmap:
	def __init__(self, width, height, number_of_mines):
		self.height = height
		self.width = width
		seed = sample(range(width * height), number_of_mines)
		minesmap = tuple(tuple(Block() for j in range(height)) for i in range(width))
		for num in seed:
			minesmap[num//height][num%height].setmine()
		for x in range(width):
			for y in range(height):
				rounding = 0
				for i, j in self.around(x, y):
					rounding += minesmap[i][j].getmine()
				minesmap[x][y].setrounding(rounding)
		self._map = minesmap

	def __getitem__(self, index):
		x, y = index
		return self._map[x][y]

	def around(self, x, y):
		return [(i, j) for j in range(max(0, y - 1),min(self.height, y + 2)) for i in range(max(0, x - 1),min(self.width, x + 2)) if i != x or j != y]

	def getnumber(self, x, y):
		return self._map[x][y].getrounding()

	def revive(self, x, y):
		block = self._map[x][y]
		if block.revived():
			return
		block.revive()
		if not block.getrounding():
			for i, j in self.around(x, y):
				self.revive(i, j)

	def setflag(self, x, y):
		self._map[x][y].setflag()

	def flagrevive(self, x, y):
		for i, j in self.around(x, y):
			if not self._map[i][j].getflag():
				self.revive(i, j)

	def outer(self):
		s = ''
		for i in range(self.width):
			for j in range(self.height):
				block = self._map[i][j]
				if not block.revived():
					s += 'p' if block.getflag() else '*'
				elif block.getmine():
					s += 'M'
				else:
					rounding = block.getrounding()
					s += str(rounding) if rounding else ' '
			s += '\n'
		return s[:-1]

	def inner(self):
		s = ''
		for i in range(self.width):
			for j in range(self.height):
				block = self._map[i][j]
				if block.getmine():
					s += 'M'
				else:
					rounding = block.getrounding()
					s += str(rounding) if rounding else ' '
			s += '\n'
		return s[:-1]

if __name__ == '__main__':
	test = Minesmap(10,10,10)
	