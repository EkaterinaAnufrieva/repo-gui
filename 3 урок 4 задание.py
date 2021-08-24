def my_func(x, y):
    return x ** y


x = float(input("vvedite chislo x "))
y = int(input("vvedite chislo y "))

print(my_func(x, y))  # 1 вариант

print("Решение через цикл")

def my_func2(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(my_func2(float(input("vvedite chislo x ")), int(input("vvedite chislo y "))))


