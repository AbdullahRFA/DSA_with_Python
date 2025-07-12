n = int(input("Enter the number of row: "))
m = int(input("Enter the number of col: "))

mat = []

for i in range(n):
    row = []
    for j in range(m):
        val = int(input(f"Enter the value for {i},{j} index: "))
        row.append(val)
    mat.append(row)
print("Give matrix: ")
for i in range(n):
    for j in range(m):
        print(mat[i][j],end=" ")
    print()

matric_sum =0
for i in range(n):
    for j in range(m):
        matric_sum+=mat[i][j]
print("Matrix sum : ",matric_sum)

for i in range(n):
    row_sum = 0
    for j in range(m):
        row_sum+=mat[i][j]
    print(f"{i} row sum : ",row_sum)

sum_of_pricipal_diagonal = 0
for i in range(n):
    for j in range(m):
        if i==j:
            sum_of_pricipal_diagonal+=mat[i][j]
print("sum_of_pricipal_diagonal",sum_of_pricipal_diagonal)

sum_of_secondary_diagonal = 0
col = len(mat[0])-1
for i in range(n):
    sum_of_secondary_diagonal+=mat[i][col-i]
print("sum_of_secondary_diagonal",sum_of_secondary_diagonal)


sum_of_upper_triangle = 0
for i in range(n):
    for j in range(m):
        if i<=j:
            sum_of_upper_triangle+=mat[i][j]
print("sum_of_upper_triangle",sum_of_upper_triangle)

sum_of_lower_triangle = 0
for i in range(n):
    for j in range(m):
        if i>=j:
            sum_of_lower_triangle+=mat[i][j]
print("sum_of_lower_triangle",sum_of_lower_triangle)