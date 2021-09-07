class Worker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name= name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position (Worker):
    def get_full_name(self):
        return "{0} {1}".format(self.name,self.surname)

    def get_total_income(self):
        return self._income["wage"]+self._income["bonus"]

worker= Position("Ivan","Ivanov","specialist", 50000, 10000)
print(worker.name)
print(worker.surname)
print(worker._income)
print(worker.position)
print(worker.get_full_name())
print(worker.get_total_income())