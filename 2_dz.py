my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list2 =  [my_list[i+1] for i in range(len(my_list) - 1) if my_list[i+1] > my_list[i]]
print(my_list2)

