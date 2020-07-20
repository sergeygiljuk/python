my_dict = {}
with open("text6.txt", "r+") as f_obj:
	content = f_obj.readlines()
	content = [el[:-1] for el in content]
	print(type(content))
	print(content)
	for i in content:
		key, val = i.split(': ')
		my_dict[key] = [int(el) for el in val.split() if el.isdigit()]
		#my_dict[key] = list(val.split())
	for key in my_dict:
		my_dict[key] = sum(my_dict[key])
	print(my_dict)
