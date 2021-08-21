input_user = input("Введите список")
input_list = list(input_user)
len_list = len(input_list)  # длина списка
i = 0  # индекс
if len_list > 1:
    while i < len_list-1:
        input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
        i+= 2
print(input_list)

#2 zadanie