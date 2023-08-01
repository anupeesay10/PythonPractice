def sum_of_n_range(n):
    sum_n=0
    for i in range(1,n+1):
        sum_n =sum_n +i
    return sum_n

if __name__== "__main__":
    max_n=int(input("Enter a value of n:"))
    series_sum_range=sum_of_n_range(max_n)
    print(series_sum_range)

