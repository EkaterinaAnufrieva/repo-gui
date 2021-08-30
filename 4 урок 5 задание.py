from functools import reduce


def my_funk(x, y):
    return x * y


gen_my_list = [i for i in range(100 - 1, 1000 + 1) if i % 2 == 0]

print(reduce(my_funk, gen_my_list))
