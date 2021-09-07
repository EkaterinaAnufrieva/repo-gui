class Stationery:
    def __init__(self, title):
        self.title = title

        def draw(self):
            print("Start drawing")

class Pen(Stationery):
    def draw(self):
        print("Start drawing with pen")

class Pencil(Stationery):
    def draw(self):
        print("Start drawing with pencil")

class Handle(Stationery):
    def draw(self):
        print("Start drawing with Handle")

pen = Pen("A")
pencil = Pencil("B")
handle = Handle("C")
for s in (pen, pencil, handle):
    s.draw()



