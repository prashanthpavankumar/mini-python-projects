import numpy as np
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
elements = []
for i in range(row):
    row = []
    for j in range(col):
        row.append(int(input(f"Enter element for position ({i+1}, {j+1}): ")))
    elements.append(row)
matrix = np.array(elements)
print("The matrix is:")
for rows in matrix:
    for vals in rows:
        print(vals, end=' ')
    print()
print("The transpose of the matrix is:")
transpose=matrix.T
for rows in transpose:
    for vals in rows:
        print(vals.T, end=' ')
    print()
print("The sum of the elements in matrix is:",np.sum(matrix))
print("The mean of the elements in them matrix",np.mean(matrix))
print("Sum of rows",np.sum(matrix,axis=1))
print("Sum of columns",np.sum(matrix,axis=0))
