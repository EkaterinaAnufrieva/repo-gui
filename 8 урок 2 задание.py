class Iskluchenie():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def error(self, a, b):
        try:
            (a/b)
        except:
            print("Деление на ноль запрещено")
        else:
            print(f"Все хорошо. Результат: {a/b}")


d = Iskluchenie(10,15)
d.error(10,15)
p = Iskluchenie(15,0)
p.error(15,0)

