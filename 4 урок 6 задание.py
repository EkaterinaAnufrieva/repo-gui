from itertools import count, cycle
chislo=int(input("Введите целое число от 1 до 15"))
for el in count(chislo): #итератор, генерирующий целые числа, начиная с указанного
    if el > 15:
        break
    else:
        print(el)
spisok = input("Введите список каких-либо элементов")
spisok_1 = spisok.split()
c = 0
for el in cycle(spisok_1): #  итератор, повторяющий элементы некоторого списка, определенного заранее
    if c > 10:
        break
    print(el)
    c = c+1
