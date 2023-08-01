def reverse_number (val):
    s=""
    for i in range(len(val)-1,-1,-1):
        s = s + val[i]
    return s

def reverse_number_1(val):
    s=""
    for i in range(len(val)):
        s = val[i] + s
    return s


if __name__ =="__main__":
    value = input("Enter an integer:")
    rev_num = reverse_number(value)
    rev_num_1 = reverse_number_1(value)
    print(rev_num)
    print(rev_num_1)



