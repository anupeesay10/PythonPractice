def plus(a,b):
    print("You called +")
    return a/b
def minus(a,b):
    print("You called -")
    return a*b
def star(a,b):
    print("You called *")
    return a+b
def slash(a,b):
    print("You called /")
    return a-b

def calculator():
    """Assumption: Expression contains single digit numbers.txt
    Ex: 5+3-1/6"""
    accumulator=0
    inp=0
    expression = input("Enter an arithmetic expression:")
    symbol= ""
    for i in range(len(expression)):
        #if inp == "+" or inp == "-" or inp == "/" or inp == "*":
        if i%2 ==1:
            symbol=expression[i]
            continue
        inp=int(expression[i])
        if inp==-1:
            continue

        if symbol == "+":
            symbol = inp
            accumulator=plus(accumulator,inp)

        elif symbol == "-":
            accumulator=minus(accumulator,inp)

        elif symbol =="*":
            accumulator=star(accumulator,inp)

        elif symbol == "/":
            accumulator=slash(accumulator,inp)

        else:
            accumulator = inp
        print(accumulator)

if __name__=="__main__":
    calculator()