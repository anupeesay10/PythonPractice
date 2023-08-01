import random
r = random.randint(0,100)
chances=0
while chances<5:
    user_input = input("Enter number between 0 and 100:")
    user_input = int(user_input)
    if user_input==r:
        print("winner")
        break
    if user_input<r:
        print("too low")
    else:
        print("too high")
    chances=chances+1
if chances==5:
    print("LOSER")
