def func_1(name, lastname, b_year, city, email, number):
	info = f"Имя {name} Фамилия {lastname} год рождения {b_year} родной город {city} email {email} номер телефона {number}"
	return(info)

print(func_1(name = input("Input your name: "), lastname = input("lastname: "), b_year = input("year of birth: "), city = input("city "), email = input("email: "), number = input("Phone number: ")))