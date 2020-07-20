class Road:
	def __init__(self, length, width):
		self._length = length
		self._width = width

	def calc(self):
		full_calc = self._length * self._width * 25 * 5 / 1000
		return f"Расчет массы асфальта завершен. {int(full_calc)}т."

road = Road(1000, 30)
print(road.calc())	


