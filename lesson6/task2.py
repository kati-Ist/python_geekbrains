class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self):
        print(f"Для асфальта потребуется {self._length * self._width * 5 * 25 // 1000} тонн")


a = Road(20, 5000)
a.asphalt()
