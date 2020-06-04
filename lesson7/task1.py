class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __add__(self, other):
        return Matrix(list(map(str,
                               [self.my_matrix[i][j] + other.my_matrix[i][j] for i in range(len(self.my_matrix)) for j
                                in range(len(self.my_matrix[i]))])))

    def __str__(self):
        if len(self.my_matrix[0]) > 1:
            return ' '.join(list(map(str, [self.my_matrix[i][j] for i in range(len(self.my_matrix)) for j in
                                           range(len(self.my_matrix[i]))])))
        else:
            return ' '.join(list(map(str, [self.my_matrix[i] for i in range(len(self.my_matrix))])))


a_1 = Matrix([[4, 1], [3, 7], [8, 9]])
a_2 = Matrix([[5, 7], [10, 6], [1, 4]])
print(a_1)
print(a_2)
print(a_1 + a_2)
