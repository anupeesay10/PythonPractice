def sum_of_n(n):
    seq=1
    sum_n=0
    while seq<= n:
        sum_n=sum_n+seq
        seq=seq+1
    return sum_n
if __name__=="__main__":
    max_n=int(input("Enter a value of n:"))
    series_sum=sum_of_n(max_n)
    print(series_sum)

