import time


class TrafficLight:
	__collor = ""

	def TLwork(self):
		print("Красный")
		time.sleep(7)
		print("Желтый")
		time.sleep(2)
		print("Зеленый")
		time.sleep(7)


tl = TrafficLight()
tl.TLwork()

