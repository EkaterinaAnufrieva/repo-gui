def my_funk():
    sum_ = 0
    ext = False
    while ext == False:
        numb = input('введите числа через пробел или # - для выхода ').split()
        i = 0
        for el in range(len(numb)):
            if numb[el] == '#':
                ext = True
                break
            else:
                i = i + int(numb[el])
        sum_ = sum_ + i
        print(f'сумма чисел = {sum_}')
    return sum_

print(my_funk())