def get_str():
	string1 = input("Введите числа через пробелы ")
	string1 = ''.join(string1.split())
	my_list = list(string1)
	for i in range(len(my_list)):
		my_list[i] = int(my_list[i])
	summ = sum(my_list)
	print(summ)
	user_answ = input("Введите w, для выхода\nЕсли хотите продолжить, введите числа через пробел: ")
	string2 = ''.join(user_answ.split())
	my_list2 = list(string2)
	if "w" in my_list2:
		my_list2.remove("w")
	for y in range(len(my_list2)):
		my_list2[y] = int(my_list2[y])
	summ2 = sum(my_list2)
	summ = summ + summ2




	return (summ)
print(get_str())