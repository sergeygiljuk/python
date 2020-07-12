def power_rise(x, y):
	while (x.isdigit() == False and  y[0] != "-"):
		x = input("Введите действительное число x: ")
		y = input("Введите отрицательное число y: ")
	z = float(x) ** int(y)
	return(z)

def power_rise2(x, y):
	z = int()
	while  (x.isdigit() == False and  y[0] != "-"): #Знаю что пользователь может ввести строку из символов начав с "-",
	# но лучше проверки на отрицатльность не нашел
		x = input("Введите действительное число x2: ")
		y = input("Введите отрицательное число y2: ")
	z2 = float(x)
	i = 1
	while i > int(y):
		z2 = z2 / float(x)
		i = i - 1
	return(z2)

#print(power_rise(input(), input()))

print(power_rise2(input(), input()))

