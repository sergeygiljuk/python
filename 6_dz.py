dict_type = dict()
start = input("Вас приветствует Jarvis v0.6. Я могу создать для вас список товаров. Хотите начать? (Y/N): ")
i = 0
final_list = list()
if start == "Y":
	number_of_tuple = int(input("Введите количество товаров в списке: "))
	while i < number_of_tuple:
		dict_type.update({"name": input("Название: "), "price" : input("Цена: "), "count": input("Количество: "), "units": input("Еденицы: ")})
		i = i + 1
		cortege = ((i), dict_type)
		final_list.append(cortege)
	print(*final_list, sep = "\n", end = "\n")
for x in final_list:
	x[1] ....???
