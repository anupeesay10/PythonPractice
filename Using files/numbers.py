def sum_multiplication(file_name):
    sum = 0
    p = 1
    f = open(file_name, "r")
    for line in f.readlines():
        for number in line.split(','):
            sum = sum + int(number)
        print(sum)
        p = p * sum  # 1 times 6, and 6 times 15 (6 becomes the new p)
        sum = 0
    print(p)

    """How can you add the numbers for each line seperately?"""


if __name__ == "__main__":
    sum_multiplication("In/numbers.txt")