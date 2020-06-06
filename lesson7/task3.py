class Cell:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other):
        ''' Сложение '''
        try:
            if self.cell_count == 0 or other.cell_count == 0:
                return "Клетки не должны быть нулями"
            else:
                return Cell(self.cell_count + other.cell_count)
        except TypeError:
            return "Вводите только целое положительное число"

    def __sub__(self, other):
        ''' Вычитание '''
        try:
            if self.cell_count == 0 or other.cell_count == 0:
                return "Клетки не должны быть нулями"
            elif self.cell_count < other.cell_count:
                return "Вторая клетка не должны быть больше первой"
            else:
                return Cell(self.cell_count - other.cell_count)
        except TypeError:
            return "Вводите только целое положительное число"

    def __mul__(self, other):
        ''' Умножение '''
        try:
            if self.cell_count == 0 or other.cell_count == 0:
                return "Клетки не должны быть нулями"
            else:
                return Cell(self.cell_count * other.cell_count)
        except TypeError:
            return "Вводите только целое положительное число"

    def __truediv__(self, other):
        ''' Деление '''
        try:
            if self.cell_count < other.cell_count:
                return "Вторая клетка не может быть больше первой"
            else:
                return Cell(self.cell_count // other.cell_count)
        except ZeroDivisionError:
            return "Клетка не должна быть нулем"
        except:
            return "Вводите только целое положительное число"

    def __str__(self):
        return str(self.cell_count)

    def make_order(self, score):
        try:
            for i in range(self.cell_count // score):
                print("*" * score)
            print("*" * (self.cell_count % score))
        except ZeroDivisionError:
            return print("Клетка не должна быть нулем")
        except:
            return print("Вводите только целое положительное число")


cell_1 = Cell(42)
cell_2 = Cell(10)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

cell_1.make_order(5)
