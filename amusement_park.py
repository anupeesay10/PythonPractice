def number_of_people_cost(num_people):
    if num_people<4:
        cost1=num_people*45
    elif num_people>=4 and num_people<6:
        cost1=num_people*40
    elif num_people>=6:
        cost1=num_people*35
    return cost1


def girls_or_boys_cost(n_b,n_g):
    cost=0
    if n_b == n_g:
        cost = -3*(n_b+n_g)
    elif n_b ==0 or n_g ==0:
        cost = -2*(n_b+n_g)
    return cost


def lunch_package_cost(lunch_package,num_people):
    cost3=0
    if lunch_package.lower() == "yes":
        cost3=10*num_people
    return cost3


def all_rides_cost(all_rides,num_people):
    cost5=0
    if all_rides.lower()=="yes":
        cost5=25*num_people
    return cost5


def lunch_package_total(lunch_package, total_cost_1):
    total1=0
    if lunch_package.lower()=="yes":
        total1=-.05*total_cost_1
    return total1

def all_rides_total(all_rides, total_cost_1):
    total2=0
    if all_rides.lower()=="yes":
        total2=-.1*total_cost_1
    return total2

def lunch_all_rides(all_rides,lunch_package,total_c_1):
    total3=0
    if all_rides.lower()=="yes" and lunch_package.lower()=="yes":
        total3=-.2*total_c_1
    return total3


if __name__ == "__main__":
    number_people = int(input("Enter the number of people in the group:"))
    cost1=number_of_people_cost(number_people)
    n_boys = int(input("Enter the number of boys"))
    n_girls = int(input("Enter the number of girls"))
    cost2=girls_or_boys_cost(n_boys, n_girls)
    lunch_package=input("Do you want a lunch package")
    cost3=lunch_package_cost(lunch_package, number_people)
    all_rides=input("Do you want all rides?")
    cost5=all_rides_cost(all_rides,number_people)
    total_cost_1=cost1+cost2+cost3+cost5
    total1=lunch_package_total(lunch_package,number_people)
    total2=all_rides_total(all_rides,number_people)
    total3=lunch_all_rides(all_rides,lunch_package,total_cost_1)
    total_cost_2=cost1+cost2+cost3+cost5+total1+total2+total3
    print("Your total cost is %d dollars." %(total_cost_2))

