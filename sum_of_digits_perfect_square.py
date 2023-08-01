def sum_of_digits(val):
    s = 0
    for i in range(len(val)):
        s = s + int(val[i])
    return s


def sum_perfect_square(sem):
    if (sem**.5)/1 != (sem**.5)//1:
        print("The sum of digits, %s is not perfect square" % sem)
    else:
        print("The sum of digits, %s is a perfect square" % sem)



if __name__ == "__main__":
    value = input("Enter an integer:")
    s_digits = sum_of_digits(value)
    print("Your sum of digits is: %s" %(s_digits))
    sum_perfect_square(s_digits)