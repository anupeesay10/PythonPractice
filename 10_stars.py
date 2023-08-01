def ten_stars_ten_rows(num):
    number_of_stars = int(num)
    number_of_rows = int(num)
    # print("%d : " %(number_of_stars), end = "")
    for row_count in range(number_of_rows):
        for star_count in range(number_of_stars):
            print("*", end = "")
        print() #What does this mean? This makes it go to the next line after a row is completed

def ten_stars_ten_rows_modified(diag):
    number_of_stars = int(diag)
    number_of_rows = int(diag)
    # print("%d : " %(number_of_stars), end = "")
    for row_count in range(number_of_rows):
        for spaces in range(number_of_rows, row_count, -1):
            print(" ", end = "")
        for star_count in range(number_of_stars):
            print("*", end = "")
        print()


if __name__ == "__main__":
    number1 = input("Enter a number of stars")
    ten_stars_ten_rows(number1)
    number2 = input("Enter a number of stars")
    ten_stars_ten_rows_modified(number2)