delimoe = float(input("Введите делимое "))
delitel = float(input("Введите делитель "))

while delitel == 0:
    print("Деление на 0 запрещено. Введите число отличное от 0 ")
    delitel = float(input("Введите делитель "))


def chastnoe(a, b):
    return a / b


print(round((chastnoe(delimoe, delitel)), 2))
