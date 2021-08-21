raiting_list = [9, 9, 8, 6, 5, 4, 4, 1]

raiting = int(input("Введите число"))
inserted = False
for index, elem in enumerate(raiting_list):
    if raiting > elem:
        raiting_list.insert(index, raiting)
        inserted = True
        break

if not inserted:
    raiting_list.append(raiting)

print(raiting_list)

#5 zadanie