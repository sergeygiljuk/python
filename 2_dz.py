from abc import ABC, abstractmethod

class Clothing(ABC):
	def __init__(self, param):
		self.param = param

	@abstractmethod
	def result(self):
		pass

	def __add__(self, other):
		return self.result + other.result


class UpSuit(Clothing):
	@property
	def result(self):
		print(f"Материала на пальто {(self.param/6.5) + 0.5}")
		return (self.param/6.5) + 0.5

class Suit(Clothing):
	@property
	def result(self):
		print(f"Материала на кастюм {(self.param * 2) + 0.3}")
		return (self.param * 2) + 0.3


suit_1 = Suit(100)
upsuit_1 = UpSuit(200)
print("%.2f" % (suit_1 + upsuit_1) + " м2")