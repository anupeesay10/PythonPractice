"""def sum_of_n(n):
    seq=1
    sum_n=0
    while seq<=n:
        sum_n=sum_n+((1)/(seq*seq))
        seq=seq+1
    return sum_n"""

def sum_of_n_range(n):
    sum_n=0
    for i in range (1,n+1):
        sum_n=sum_n+((1)/(i*i))
        i=i+1
    return sum_n
if __name__ == "__main__":
        max_n = int(input("Enter a value of n:"))
        series_sum_range = sum_of_n_range(max_n)
        """series_sum_while=sum_of_n(max_n)
        print(series_sum_while)"""
        print(series_sum_range)