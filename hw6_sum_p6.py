def sum_of_n(n):
    seq=9
    sum_n=0
    while seq<= 10*n:
        sum_n=sum_n+seq
        seq=seq+10
    return sum_n

def sum_of_n_range(n):
    sum_n=0
    for i in range (9,10*n,10):
        sum_n=sum_n+i
    return sum_n
if __name__ == "__main__":
        max_n = int(input("Enter a value of n:"))
        series_sum_range = sum_of_n_range(max_n)
        series_sum_while=sum_of_n(max_n)
        print(series_sum_while)
        print(series_sum_range)