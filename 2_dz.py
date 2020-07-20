with open("text2.txt", "r") as f_obj:
	content = f_obj.readlines()
	for line in content:
		print(f"В строке {line} {len(line) - 1} символов")
	print(f"В файле {len(content)} строк")