def my_func(arg_1, arg_2, arg_3):
	box_list = [arg_1, arg_2, arg_3]
	box_list.remove(min(box_list))
	return(box_list)

print(my_func(55,70,50))