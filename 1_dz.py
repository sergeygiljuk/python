def my_func(s_1, s_2):
    while s_2 == "0" or (s_1.isdigit() and s_2.isdigit()) == False :
        s_1 = input("Введите числа\nПервое: ")
        s_2 = input("Второе (не 0): ")
    s_3 = int(s_1) / int(s_2)
    return (s_3)  
    

print(my_func(input("Введите числа для деления.\nПервое число: "), input("Второе число: ")))
