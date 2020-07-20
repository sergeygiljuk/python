with open("text5.txt", "w+") as f_obj:
	input_str = input("Введите числа через пробел: ")
	f_obj.writelines(input_str)
	in_list = input_str.split(" ")
	in_list = [int(x) for x in in_list]
with open("text5result.txt", "w+") as f2_obj:
	print(sum(in_list), file = f2_obj)
