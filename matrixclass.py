import random

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = self.generate_random_matrix()

    def generate_random_matrix(self):
        matrix = [[random.randint(1, 100) for _ in range(self.m)] for _ in range(self.n)]
        return matrix

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def calculate_mean(self):
        total_sum = 0
        for row in self.matrix:
            total_sum += sum(row)
        return total_sum / (self.n * self.m)

    def sum_row(self, row_index):
        if row_index < 0 or row_index >= self.n:
            return None
        return sum(self.matrix[row_index])

    def average_column(self, col_index):
        if col_index < 0 or col_index >= self.m:
            return None
        col_sum = sum(row[col_index] for row in self.matrix)
        return col_sum / self.n

    def print_submatrix(self, col_range, row_range):
        col1, col2, row1, row2 = col_range[0], col_range[1], row_range[0], row_range[1]
        if col1 < 0 or col2 >= self.m or row1 < 0 or row2 >= self.n:
            print("Invalid submatrix range")
            return
        for row in self.matrix[row1:row2 + 1]:
            print(row[col1:col2 + 1])



matrix = Matrix(3, 4)
print("Generated Matrix:")
matrix.print_matrix()

print("\nMean of the Matrix:", matrix.calculate_mean())

row_index=int(input("Enter the index of row:"))
sum_of_row = matrix.sum_row(row_index)
print(f"Sum of row {row_index + 1}: {sum_of_row}")

col_index=int(input("Enter the index of column:"))
average_of_column = matrix.average_column(col_index)
print(f"Average of column {col_index + 1}: {average_of_column}")
