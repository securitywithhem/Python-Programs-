# matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
# for row in matrix:
#     print(row)



#Qa
def matrix_find(i,j,k):
    matrix = [[i,j,k],[k,i,j],[j,k,i]]
    for row in matrix:
        print(row)
    
i = int(input("Enter the Frist Number :  "))
j = int(input("Enter the second Number : "))
k = int(input("Enter the third Number :  "))
result = matrix_find(i,j,k)
print(f'FinalMAtrix : {result}')   


#Qb



import numpy as np 

def arrange_numbers(n, numbers):
    # Create an empty matrix
    matrix = np.zeros((n, n), dtype=int)

    # Fill the matrix in a cyclic manner
    for i in range(n):
        for j in range(n):
            matrix[i, j] = numbers[(i + j) % n]

    return matrix

# Example usage
n = 5
numbers = list(range(1, n+1))  # [1, 2, 3, 4, 5]
matrix = arrange_numbers(n, numbers)
print(matrix)

#Qc

import numpy as np

def create_9x9_matrix():
    # Define the 9 unique numbers
    numbers = list(range(1, 10))

    # Create the 9x9 matrix
    matrix = np.zeros((9, 9), dtype=int)

    # Fill the matrix in a cyclic manner
    for i in range(9):
        for j in range(9):
            matrix[i, j] = numbers[(i + j) % 9]

    return matrix

def check_3x3_matrices(matrix):
    # Split the 9x9 matrix into 9 3x3 matrices
    matrices = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            matrices.append(matrix[i:i+3, j:j+3])

    # Check each 3x3 matrix
    for mat in matrices:
        if not (len(set(mat[:, 0])) == 3 and len(set(mat[:, 1])) == 3 and len(set(mat[:, 2])) == 3):
            return False
        if not (len(set(mat[0, :])) == 3 and len(set(mat[1, :])) == 3 and len(set(mat[2, :])) == 3):
            return False

    return True

# Create the 9x9 matrix
matrix = create_9x9_matrix()

# Check the 3x3 matrices
if check_3x3_matrices(matrix):
    print("Each 3x3 matrix has different numbers in each row and each column")
else:
    print("Not all 3x3 matrices have different numbers in each row and each column")