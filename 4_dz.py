class Auto:


	def __init__(self, name, color, speed, police = False):
		self.name = name
		self.color = color
		self.speed = speed
		self.police = police

	def go(self):
		print(f"{self.name} поехала {'полиция' if self.police == True else ''}")

	def stop(self):
		print(f"{self.name} остановилась")

	def turn(self, where_turn):
		print(f"{self.name} повернула {'направо' if where_turn == 0 else 'налево'}")

	def show_speed(self):
		return f"Скорость: {self.speed}"


class TownCar(Auto):

	def show_speed(self):
		return f"Скорость автомобиля: {self.speed}. Превышение скорости" if self.speed > 60 else f"Скорость автомобиля: {self.speed}"

class WorkCar(Auto):

	def show_speed(self):
		return f"Скорость автомобиля: {self.speed}. Превышение скорости" if self.speed > 40 else f"Скорость автомобиля: {self.speed}"

class SportCar(Auto):
	"""ssss"""

class PoliceCar(Auto):

	def __init__(self, name, color, speed, police = True):
		super().__init__(name, color, speed, police)
		



police_car = PoliceCar("Лада", "серый", 100)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work = WorkCar("Камаз", "белый", 100)
work.go()
print(work.show_speed())
work.turn(1)
work.stop()
print()


town = TownCar("Мерен", "черный", 50)
town.go()
print(town.show_speed())
town.turn(0)
town.stop()
print()


sprot = SportCar("Ламба", "Желтый", 50)
sprot.go()
print(sprot.show_speed())
sprot.turn(0)
sprot.stop()
print()