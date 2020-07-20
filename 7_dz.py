my_dict = {}
with open("text7.txt", "r+") as f_obj:
	content = f_obj.readlines()
	content = [el[:-1] for el in content]
	print(content)
	for i in content:
		i = i.split()
		if (int(i[2]) - int(i[3]) > 0):
			result = int(i[2]) - int(i[3]
			my_dict[i[0]] = result

	print(my_dict)
	print(type(content))
	print(content)
	