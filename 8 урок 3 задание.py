class Exception():
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите числа. Чтобы завершить программу, введите "stop" '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                error = input(f"Вы ввели не число. Введите число или введите 'stop' для завершения программы ")
                if error == 'stop':
                    return f'Программа завершена'
                else:
                    print(try_except.my_input())



try_except = Exception()
print(try_except.my_input())
