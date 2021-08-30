def generator(n):
    c=1
    for el in range(1,n+1):
        c=c*el
        yield c



factorial=int(input("Для вычисления факторила, введите число "))

for id, elem in enumerate(generator(factorial)):
    print(f"{id+1} {elem}")

