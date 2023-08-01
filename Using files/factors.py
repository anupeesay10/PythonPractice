def get_factors(my_num):
    for i in range(1, my_num//2 + 1, 1):
        if my_num % i == 0:
            print(i, end = ",")
    print(my_num)

def get_factor_sum(my_num):
    sum = 0
    for i in range(1, my_num + 1, 1):
        if my_num % i == 0:
            print(i, end=",")
            print(my_num)
            # for f in range(len(str(my_num))):
            #     if ord(str(my_num)) >= 48 and ord(str(my_num)) <= 52:
            #         sum = sum + int(my_num)
            #         print(int(sum))


def get_common_multiple(file_name):
    multiple = 0
    f = open(file_name, "r")
    for character in f.readlines(): #Use the split to get the numbers.
        if ord(character) >= 48 and ord(character) <= 57:
            multiple = character + character
            print(multiple)



if __name__ == "__main__":
    number = int(input("Enter a whole number:"))
    get_factors(number)
    """numbers = int(input("Enter a whole number:"))
    get_factor_sum(numbers)"""
    get_common_multiple("In/common_multiple_numbers.txt")