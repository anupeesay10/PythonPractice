def names_meet(file_name):
    f = open(file_name, "r")
    for line in f.readlines():
        names = line.split(',')
    for i in range(len(names)):
        names[i] = names[i].strip()  #strip() with empty parenthesis takes away all invisible characters.
    for n1 in range(len(names) - 1):
        for n2 in range(n1 + 1, len(names)):
            print(names[n1], names[n2])
        # print("%s meets %s" %(name[0],name[1]))
        # print("%s meets %s" %(name[0],name[2]))
        # print("%s meets %s" %(name[1],name[2]))





if __name__ == "__main__":
    names_meet("In/names.txt")