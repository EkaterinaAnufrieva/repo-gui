class Data:
    def __init__(self, dd_mm_gg):
        self.dd_mm_gg = dd_mm_gg

    @classmethod
    def extract(cls, dd_mm_gg ):
        my_date = []

        for i in dd_mm_gg.split():
            if i != '-' : my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if (day>=1 and day <= 31) and (1 <= month <= 12) and (2021 >= year >= 0):
            return f'Дата введена корректно'
        else:
            return f'Дата введена некорректно'



print(Data.valid(40, 11, 2021))
print(Data.valid(12, 9, 2021))
print(Data.extract('12 - 9 - 2011'))







