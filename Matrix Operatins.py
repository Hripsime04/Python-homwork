import random

def generate_random_matrix(rows, cols):
    matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
    return matrix

def get_column_sum(matrix, column_index):
    if column_index < 0 or column_index >= len(matrix[0]):  
        return None 

    column_sum = 0
    for row in matrix:
        column_sum += row[column_index]
    return column_sum  

def get_row_average(matrix,row_index):
    if row_index < 0 or row_index >= len(matrix):
        return None 
    
    row_sum = 0
    row_length = len(matrix[row_index])
    for value in matrix[row_index]:
        row_sum += value
    
    row_average = row_sum / row_length
    return row_average
  

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

random_matrix = generate_random_matrix(rows, cols)
print("Generated random matrix:")
for row in random_matrix:
    print(row)

column_index = int(input("Enter the index of column: "))
sum_of_column = get_column_sum(random_matrix, column_index)
print(f"Sum of column {column_index + 1}: {sum_of_column}")

row_index=int(input("Enter the index of row:"))
average_of_row=get_row_average(random_matrix,row_index)
print(f"average of row {row_index + 1}: {average_of_row}")
