class Stationary:
	def __init__(self, title = "Рисовалка"):
		self.title = title

	def draw(self):
		print(f"Запуск отрисовки")

class Pen(Stationary):
	def draw(self):
		print(f"Запуск отрисовки {self.title}")

class Pencil(Stationary):
	def draw(self):
		print(f"Запуск отрисовки {self.title}")

class Handle(Stationary):
	def draw(self):
		print(f"Запуск отрисовки {self.title}")


kanz = Stationary()
kanz.draw()
pen = Pen("шарик")
pen.draw()
pencil = Pencil("серый")
pen.draw()
handle = Handle("выделитель")
handle.draw()