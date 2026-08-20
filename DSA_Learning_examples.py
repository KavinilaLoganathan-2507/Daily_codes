
# *Array 

#Let us say your expense for every month are listed below,
#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190
#Create a list to store these monthly expenses and using that find out,

#1. In Feb, how many dollars you spent extra compare to January?
#2. Find out your total expense in first quarter (first three months) of the year.
#3. Find out if you spent exactly 2000 dollars in any month
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

# Syntax for integer elements
arr = list(map(int, input("Enter space-separated numbers: ").split()))

# Syntax for string elements
arr = input("Enter space-separated strings: ").split()

#----------------------------------------------------------------------------------------------------------------------------------------------------

monthly_expense = [2200, 2350, 2600, 2130, 2190]

# 1
print(monthly_expense[1] - monthly_expense[0])

# 2
print(sum(monthly_expense[:3])) # res = monthly_expense[0] + monthly_expense[1] + monthly_expense[2]

# 3
if 2000 in monthly_expense:
    print("Spent exactly $2000")
else:
    print("Did not spend exactly $2000")

# 4
monthly_expense.append(1980)
print(monthly_expense)

# 5
monthly_expense[3] =  monthly_expense[3] - 200 
print(monthly_expense)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

# Create two 2x2 matrices
A = np.array([[1, 2], 
              [3, 4]])
              
B = np.array([[5, 6], 
              [7, 8]])*

# 1. Addition
add_result = A + B

# 2. Subtraction
sub_result = A - B

# 3. Element-wise Multiplication
element_mult = A * B

# 4. Matrix Multiplication (Dot Product)
dot_product = A @ B  
# Note: np.dot(A, B) also does the exact same thing

# 5. Transpose (Swapping rows and columns)
transpose_A = A.T

# Sample 2x2 Matrices
A = [[1, 2], 
     [3, 4]]
     
B = [[5, 6], 
     [7, 8]]

# 1. Addition (Element-wise)
def add_matrices(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

# 2. Subtraction (Element-wise)
def subtract_matrices(mat1, mat2):
    return [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

# 3. Transpose (Swapping rows to columns)
def transpose_matrix(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

# 4. Matrix Multiplication (Dot Product)
def multiply_matrices(mat1, mat2):
    # Initialize an empty matrix of size: rows of mat1 x cols of mat2
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    
    # Iterate through rows of mat1
    for i in range(len(mat1)):
        # Iterate through columns of mat2
        for j in range(len(mat2[0])):
            # Iterate through rows of mat2
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
                
    return result

# --- Executing the functions ---
print("Addition:", add_matrices(A, B))
print("Matrix Multiplication:", multiply_matrices(A, B))
print("Transpose of A:", transpose_matrix(A))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
