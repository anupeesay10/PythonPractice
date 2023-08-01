
def largest_digit(val):
    s = ""
    for i in range(len(val)):
        if ord(val[i]) >= 48 and ord(val[i]) <= 57:
            if s < val[i]:
                s = val[i]
    return s


if __name__ == "__main__":
    value = input("Enter a positive integer:")
    large_d = largest_digit(value)
    print("The largest digit is: %s" %(large_d))
