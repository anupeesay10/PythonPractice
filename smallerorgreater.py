"""
Author: Anirudh Peesay
Description: This program finds the largest of two numbers.txt
Date: 5/25/23
Modify this program to find the largest of four numbers.txt
"""

def display_nums(n1,n2,n3,n4):
    print("%d is greater than %d and %d and %d" % (n1, n2,n3,n4))
def compare_numbers_tempvariable(n1,n2,n3,n4):
    my_max=n1
    if my_max<n2:
        my_max=n2
    if my_max<n3:
        my_max=n3
    if my_max<n4:
        my_max=n4
    return my_max
def compare_numbers_logical(n1,n2,n3,n4):
    if n1>n2 and n1>n3 and n1>n4:
        return n1
    if n2>n3 and n2>n4:
        return n2
    if n3>n4:
        return n3
    return n4
def compare_numbers_using_var(n1,n2,n3,n4):
    c=n1>n2 and n1>n3 and n1>n4
    if c:
        my_max=n1
    else:
        c=n2>n3 and n2>n4
        if c:
            my_max=n2
        else:
            c=n3>n4
            if c:
                my_max=n3
            else:
                my_max=n4
    return my_max
def compare_numbers(num_1,num_2,num_3,num_4):
    if num_1 >= num_2:
        if num_1>=num_3:
            if num_1>=num_4:
                display_nums(num_1, num_2,num_3,num_4)
    if num_2 >= num_1:
        if num_2>=num_3:
            if num_2 >= num_4:
                display_nums(num_2, num_1,num_3,num_4)
    if num_3>=num_2:
        if num_3 >= num_1:
            if num_3 >= num_4:
                display_nums(num_3,num_1,num_2,num_4)
    if num_4 >= num_1:
        if num_4 >= num_2:
            if num_4 >= num_3:
                display_nums(num_4,num_3,num_2,num_1)


if __name__=="__main__":
    num_1=input("Enter your first number")
    num_2=input("Enter your second number")
    num_3=input("Enter your third number")
    num_4=input("Enter your fourth number")
    num_1=int(num_1)
    num_2=int(num_2)
    num_3=int(num_3)
    num_4=int(num_4)
    compare_numbers(num_1,num_2,num_3,num_4)
    my_max=compare_numbers_tempvariable(num_1,num_2,num_3,num_4)
    print(my_max)