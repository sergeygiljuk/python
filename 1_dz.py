import shutil


A = [input("Введите строку: ")+"\n" for i in range(int(input("Введите количество строк: ")))]
with open("text.txt", "w") as f_obj:
	f_obj.writelines(A)
shutil.copyfile("text.txt", "text7.txt") #Использовал, для создания файликов для след заданий (лень)
#Мне показалось, что логика задания не нарушена, а решение локанично и элегантно ;)