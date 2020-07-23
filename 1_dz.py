class Matrix:
	def __init__(self, number):
		self.number = number

	def __str__(self):
		return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.number])


	def __add__(self, other):
		result = []
		for i in range(len(self.number)):
			result.append([])
			for j in range(len(self.number[0])):
				result[i].append(self.number[i][j] + other.number[i][j])
		return '\n'.join([''.join(['%d\t' % i for i in row]) for row in result])




mat1 = Matrix([[2, 2], [3, 3], [4, 4]])
mat2 = Matrix([[2, 3], [3, 4], [4, 5]])
print(mat1)
print(f"***" * 30)
print(mat2)
print(f"***" * 30)
print(mat1 + mat2)
print(f"***" * 30)
