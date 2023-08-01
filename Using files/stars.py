def stars_count(file_name):
    f = open(file_name, "r")
    num = f.read()
    num = num.strip()  # strip will take out the blank lines in the in file.
    print(num)
    for character in num:
        if ord(character) >= 48 and ord(character) <= 57:
            number_of_stars = int(character)
            print("%d : " %(number_of_stars), end = "")
            for star_count in range(number_of_stars):  #range(len) is for a string
                #range statement allows you to keep printing stars for as many as needed
                print("*", end = "")
            print()


    # character = ""
    # new_character = ""
    # for line in f.readlines():
    #     for character in line:
    #         if int(character) >= 48 and int(character) <=57:
    #             new_character = character
    #         print(new_character)

    """f.read reads all of the lines in the in file. f.readline will read one line. f.readlines will read one line at a time, and complete for all lines."""



if __name__ == "__main__":
    stars_count("In/stars_integer.txt")
