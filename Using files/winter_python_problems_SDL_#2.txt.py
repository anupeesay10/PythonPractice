def even_odd_number(file_name):
    f = open(file_name, "r")
    f_out = open("Out/new_list.csv", "w")
    the_list = f.readline()
    for word in the_list.split(","): #When you split by comma, it returns as string
        for character in word:
            if ord(character) >= 48 and ord(character) <= 57:
              # if is_number is the same as saying if is_number == True
                    word = int(word)
                    if word % 2 == 0:
                        f_out.write("%d\n" %(word))
                    else:
                        f_out.write("%d\n" %(word*2))
                    break  # This terminates the for loop
    f_out.close()
    f.close()








if __name__ == "__main__":
    even_odd_number("In/winter_python_problems_SDL_#2.txt")

