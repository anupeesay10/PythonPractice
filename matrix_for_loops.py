no_rows = int(input("Enter number of rows: "))
no_cols = int(input("Enter number of columns: "))

matrix1 = []
for r in range(no_rows):
    matrix1.append([])
    for c in range(no_cols):
        element = int(input("Enter row: %d and col: %d element: " % (r,c)))
        matrix1[r].append(element)

for r in range(no_rows):
    for c in range(no_cols):
        print(matrix1[r][c], end = " ")   #matrix1[r][c] represents each element now, denoted by the element variable created.
    print() 