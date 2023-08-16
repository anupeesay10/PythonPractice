def longest_string(file_name):
    f = open(file_name, "r")
    max_length = 0
    max_index = 0
    r = f.read()
    strings = r.split(",")
    for i in range(len(strings)):
        l = len(strings[i])
        if max_length < l:
            max_length = l
            max_index = i
    print("The longest string is: %s" %(strings[max_index]).strip())
















if __name__ == "__main__":
    longest_string("In/longest_list.txt")