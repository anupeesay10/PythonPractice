def calc_letters(expression):

    value_lower=0
    value_upper=0
    for i in range(len(expression)):
        symbol=expression[i]
        if ord(symbol)<=90 and ord(symbol)>=65:
            """UPPERCASE"""
            value_upper=value_upper+1
        if ord(symbol)>=97 and ord(symbol)<=122:
            """LOWERCASE"""
            value_lower=value_lower+1

    print(value_lower)
    print(value_upper)

if __name__ == "__main__":
    expression = input("Enter a string expression:")
    calc_letters(expression)