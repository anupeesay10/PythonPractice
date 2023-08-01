"""
Problem:
Part 1: Accept a list of numbers.txt separated by commas. Implement a function to split the numbers.txt
and convert to integers. Find the largest of given numbers.txt.
Part 2: Implement a function to find the mean of the given numbers.txt.
"""

def largest_of_n_numbers(lt):
    s=0
    for num in lt.split(","):
        print(int(num))
        if s < int(num):
            s = int(num)
    return s

"""def sum_of_n_numbers(lt):
    s=0
    for num in lt.split(","):
        print(int(num))
        s = s + int(num)
    return s"""

def mean_of_n_numbers(lt):
    s = 0
    for num in lt.split(","):
        print(int(num))
        s = s + int(num)
    count1 = 1

    for num in lt:
        if num == ",":
            count1 = count1 + 1

    meaned_up = s / count1
    print("The mean of the given numbers.txt is: %.2f" %(meaned_up)) #.2f gives answer to two decimal points



if __name__ == "__main__":
    list = input("Enter a list of numbers.txt separated by commas:")
    large_o_list = largest_of_n_numbers(list)
    print("The largest of the given numbers.txt is: %d" %(large_o_list))
    """sum_o_list = sum_of_n_numbers(list)
    print("The sum of the given numbers.txt is: %d" %(sum_o_list))"""
    mean_o_list = mean_of_n_numbers(list)


