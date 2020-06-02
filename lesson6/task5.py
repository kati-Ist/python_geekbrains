class Stationery:
    title = "канцелярская принадлежность"

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом")


class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером")


a = Stationery()
a.draw()

a = Pen()
a.draw()

a = Pencil()
a.draw()

a = Handle()
a.draw()
