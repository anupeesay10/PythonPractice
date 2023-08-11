def largest(l):
    char = 0
    for character in l.split(","):
        # print(int(character))
        if int(character) > char:
            char = int(character)  #Why does this not work the other way around?
    return char

def smallest(s):
    smol = None
    for character in s.split(","):
        if smol is None: #This will set the first integer as smol, then it will start comparing.
            smol = int(character)
        # print(int(character))
        if int(character) < smol:
            smol = int(character)
    return smol

def average(a):
    s = 0
    for character in a.split(","):
        # print(int(character))
        s = s + int(character)
    count = 1

    for character in a:
        if character == ",":
            count = count + 1

    mean =  s / count
    return mean



if __name__ == "__main__":
    list = input("Enter a list of integers separated by commas:")
    large_o_list = largest(list)
    print("The largest number is: %d." %(large_o_list))
    smol_o_list = smallest(list)
    print("The smallest number is: %d." %(smol_o_list))
    avg_o_list = average(list)
    print("The average of the list is: %f" %(avg_o_list))
