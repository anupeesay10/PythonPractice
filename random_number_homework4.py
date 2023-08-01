import random
r = random.randint(0,100)
print(r)
chances = 0
start = 0
end = 100
while True:
    x=random.randint(start,end)
    # print(x)
    if x == r:
        print("winner")
        break
    if x < r:
        print("too low")
        start = x
    else:
        print("Too high")
        end = x
    chances=chances+1
print("Took %d chances " % chances)

"""Line number 19 is used to see how many chances is being used. This is NOT for looping the iteration for an infinate number of times.
While true takes care of this."""