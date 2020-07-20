class Worker:


	def __init__(self, name, surname, posititon, wage, bonus):
		self.name = name
		self.surname = surname
		self.posititon = posititon
		self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
	def get_full_name(self):
		return f"Сотрудник {self.name} {self.surname}"


	def get_total_income(self):
		return f"Доход с премиями: {sum(self._income.values())}"

worker = Position("Причуда", "Петров", "помогатель", 20000, 300)
print(worker.get_full_name())
print(worker.posititon)
print(worker.get_total_income())