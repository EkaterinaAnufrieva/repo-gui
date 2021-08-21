key=input("Введите число от 1 до 12 ")

a, b, c, d = "зима", "весна", "лето", "осень"

my_dict = {'1': a, '2': a, '3': b, '4' : b, '5' : b, '6' : c,'7': c, '8': c, '9':d, '10': d, '11': d, '12': a}

print(my_dict[key])  # решение через словарь

my_list = [a, a, b, b, b, c, c, c, d, d, d, a]  # решение через словарь

print(my_list[int(key)-1])  

# 3 zadanie