
def matrix_1(row,col):
    matrix1 = []
    for r in range(row):
        matrix1.append([])
        for c in range(col):
            element = int(input("Enter row: %d and col: %d element: " % (r,c)))
            matrix1[r].append(element)

    for r in range(row):
        for c in range(col):
            first_matrix = matrix1[r][c]
            print(first_matrix, end = " ")   #matrix1[r][c] represents each element now, denoted by the element variable created.
        print()                          #First matrix is created.


def matrix_2(row2,col2):
    matrix2 = []
    for r2 in range(row2):
        matrix2.append([])
        for c2 in range(col2):
            element2 = int(input("Enter row: %d and col: %d element: " %(r2,c2)))
            matrix2[r2].append(element2)

    for r2 in range(row2):
        for c2 in range(col2):
            second_matrix = matrix2[r2][c2]
            print(second_matrix, end = " ")
        print()                #Second matrix is created.


def add_matrices(no_rows, no_cols):
    matrix3 = []

    for r3 in range(no_rows):
        matrix3.append([])
        for c3 in range(no_cols):
            element3 = matrix_1[r][c] + matrix_2[r2][c2]
            matrix3[r3].append(element3)

    for r3 in range(no_rows):
        for c3 in range(no_cols):
            print(matrix3[r3][c3], end=" ")
        print()





if __name__ == "__main__":
    no_rows = int(input("Enter number of rows: "))
    no_cols = int(input("Enter number of columns: "))
    no_rows2 = int(input("Enter number of rows: "))
    no_cols2 = int(input("Enter number of cols: "))
    completed_matrix_1 = matrix_1(no_rows, no_cols)
    print(completed_matrix_1)
    completed_matrix_2 = matrix_2(no_rows2, no_cols2)
    print(completed_matrix_2)
    add_matrices(no_rows, no_cols)



# matrix1 = []
# matrix2 = []
# matrix3 = []
# for r in range(no_rows):
#     matrix1.append([])
#     for c in range(no_cols):
#         element = int(input("Enter row: %d and col: %d element: " % (r,c)))
# for r2 in range(no_rows2):
#     matrix2.append([])
#     for c2 in range(no_cols2):
#         element2 = int(input("Enter row: %d and col: %d element: " %(r2,c2)))
#
#         for r3 in range(no_rows):
#             matrix3.append([])
#             for c3 in range(no_cols):
#                 element3 = element + element2
#                 matrix3[r3].append(element3)
#
#         for r3 in range(no_rows):
#             for c3 in range(no_cols):
#                 print(matrix3[r3][c3], end=" ")
#             print()








# matrix3 = []
#
# for r3 in range(no_rows):
#     matrix3.append([])
#     for c3 in range(no_cols):
#         element3 = element + element2
#         matrix3[r3].append(element3)
#
# for r3 in range(no_rows):
#     for c3 in range(no_cols):
#         print(matrix3[r3][c3], end = " ")
#     print()







