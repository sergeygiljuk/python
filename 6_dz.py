def up_reg(text):
	while text[0].isalpha() == False:
		text = input("Строка должна начинаться с буквы\nВведите заного: ")
	text = text.capitalize()
	return(text)


a = input("Введите слова через пробелы: ")

words = a.split(" ")
final_words = []
for word in words:
	final_words.append(up_reg(word))
final_text = ' '.join(final_words)
print(final_text)
