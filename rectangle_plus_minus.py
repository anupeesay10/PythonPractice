def rectangle_plus_minus(r,c):
    number_of_plus = int(r)
    number_of_cols = int(c)
    for row_count in range(number_of_plus):
        print("+", end="")

        for col_count in range(number_of_cols - 2):
            if row_count == 0 or row_count == number_of_plus - 1:
                print("-", end = "")
            else:
                print(" ", end= "")
        print("+")
    print()


def rectangle_plus_minus_modified(r,c):
    number_of_rows = int(r)
    number_of_columns = int(c)

    for pipe_count in range(number_of_rows):
        if pipe_count == 0 or pipe_count == number_of_rows - 1:
            print("+", end = "")
        else:
            print("|", end = "")

        for column_count in range(number_of_columns - 2):
            if pipe_count == 0 or pipe_count == number_of_rows - 1:
                print("-", end = "")
            else:
                print(" ", end = "")

        if pipe_count == 0 or pipe_count == number_of_rows - 1:
            print("+")
        else:
            print("|")
        # for i in range(number_of_columns):
        #     for t in range(number_of_rows):
        #         if i == 0 and t == 0:
        #             print("+")
    print()




if __name__ == "__main__":

    rows = int(input("Enter the number of rows:"))
    columns = int(input("Enter the number of columns:"))
    rectangle_plus_minus(rows, columns)

    rows2 = int(input("Enter the number of rows:"))
    columns2 = int(input("Enter the number of columns:"))
    rectangle_plus_minus_modified(rows2, columns2)

