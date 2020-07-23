class Atom:
	def __init__(self, num):
		self.num = num

	def __str__(self):

		pass

	def __add__(self, other):
		return self.num + other.num

	def __sub__(self, other):
		return self.num - other.num if self.num > other.num else print("We can`t")

	def __truediv__(self, other):
		return self.num // other.num

	def __mul__(self, other):
		return self.num * other.num

	def make_order(self, points):
		return "\n".join(["*" * points for i in range(self.num // points)]) + "\n" + "*" * (self.num % points)
	#Сам не додумался как это реализовать. =(


atom1 = Atom(50)
atom2 = Atom(32)
print(atom1 / atom2)
print(atom1.make_order(10))