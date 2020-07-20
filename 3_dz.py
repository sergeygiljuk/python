from functools import reduce

with open("text3.txt", "r") as f_obj:
	content = f_obj.readlines()
	res = {sub.split(" ")[0]: sub.split(" ")[1] for sub in content}
	for key in res:
		res[key] = int(res[key][:-1])
		if res[key] < 20000:
			print(f"{key} получает меньше 15000")
	print(f"Средняя зарплата {int(sum(res.values())/len(res.values()))}")
	print(res)