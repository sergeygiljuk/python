rus_list = ["Один", "Два", "Три", "Четыре"]
with open("text4.txt", "r+") as f_obj:
	content = f_obj.readlines()
	print(content)
	res = {sub.split(" - ")[1]: sub.split(" - ")[0] for sub in content}

	print(res)
	i = 0
	for key in res:
		
		res[key] = rus_list[i]
		i = i + 1
	print(res)
	res2 = {v:k for k, v in res.items()}
	print(res2)
with open("text4(1).txt", "w") as out:
	for key,val in res2.items():
		out.write(f"{key}:{val}")
#Нашел новый и очень удобный способ записи в файл