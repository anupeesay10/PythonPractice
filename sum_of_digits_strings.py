def sum_of_digits(val):
    s = 0
    for i in range(len(val)):
        s = s + int(val[i])
    return s


if __name__ == "__main__":
    value = input("Enter an integer:")
    s_digits = sum_of_digits(value)
    print(s_digits)

