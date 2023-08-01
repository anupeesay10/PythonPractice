num=0
sum=0
user_input=input("Enter number of numbers.txt to sum up:")
user_input=int(user_input)
while True:
    sum=sum+num
    num=num+1
    if num>user_input:
        break
print(sum)

