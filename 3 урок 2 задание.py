name = input("Введите имя ")
surname = input("Введите фамилию ")
god = input("Введите год рождения ")
gorod = input("Введите город ")
email = input("Введите email ")
telefon = input("Введите телефон ")


def user(a, b, c, d, e, g):
    return print(f'{a} {b} {c} {d} {e} {g}')



print('Данные о пользователе :')
print(user(a=name, b=surname, c=god, d=gorod, e=email, g=telefon))

