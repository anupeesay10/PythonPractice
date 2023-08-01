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







if __name__ == "__main__":

    rows = int(input("Enter the number of rows:"))
    columns = int(input("Enter the number of columns:"))
    rectangle_plus_minus(rows, columns)
