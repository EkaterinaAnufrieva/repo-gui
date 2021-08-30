my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
gen_my_list = [i for i in my_list if my_list.count(i) == 1]
print(gen_my_list)