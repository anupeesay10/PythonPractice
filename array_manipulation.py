def get_average(l):
    sum = 0
    number_count = 0
    for character in l.split(','):
        if ord(character) >= 48 and ord(character) <= 57:
            sum = sum + int(character)
    print(sum)
    for character in list:
        if ord(character) == 44:
            number_count = number_count + 1
            number_count_real = number_count + 1
    print(number_count_real)
    mean = sum / number_count_real
    print(mean)
    print("The mean of the numbers in the list is %f" %(mean))
    if int(character) >= mean:
        print("The numbers that are greater than the mean are: %d" %(int(character)))

def greater_or_smaller(l):
    sum = 0
    number_count = 0
    for character in l.split(','):
        if ord(character) >= 48 and ord(character) <= 57:
            sum = sum + int(character)
            print(sum)
    for character in list:
        if ord(character) == 44:
            number_count = number_count + 1
            number_count_real = number_count + 1
    print(number_count_real)
    mean = sum / number_count_real
    print(mean)
    print("The mean of the numbers in the list is %d" % (mean))  # Why does this not give the exact mean
    if int(character) >= mean:
        print("The numbers that are greater than the mean are: %d" % (int(character)))
    elif int(character) <= mean:
        print("The numbers that are less than the mean are %d" % (int(character)))

def cumulative_sum(l):
    sum = 0
    for character in l.split(','):
        if ord(character) >= 48 and ord(character) <= 57:
            sum = sum + (character)
            print(sum)  #How to print cumulative sum?


def reverse_order(l):
    reverse_list = ""
    for i in range(len(l)-1, -1, -1):
        reverse_list = reverse_list + l[i]
    print("The reverse list is: %s" %(reverse_list))
    if reverse_list == l:
        print("The reverse list is the same as the original list")   #Is this what prompt number 6 means?


def sum_order(l):
    character = ""
    sums = 0
    for i in range(len(l.split(','))):
        sums






if __name__ == "__main__":
    list = input("Enter a list of numbers separated by commas:")
    get_average(list)
    reverse_order(list)