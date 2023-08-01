def school_list(file_name):
    f = open(file_name, "r")
    character = ""
    for line in f.readlines():
        for char in line.split():
            if ord(char) >= 65 and ord(char) <= 90:
                character = character + char
            print(character)


if __name__ == "__main__":
    school_list("In/school_list.txt")