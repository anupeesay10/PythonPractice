"""def sum_of_n(n):
    seq=1
    sum_n=0
    prev=0
    t=1
    while seq<=n:
        if seq%2==0:
            sum_n=sum_n+(prev+1)
        else:
            prev=3*(t-1)+1
            sum_n=sum_n+prev
            t=t+1
        seq=seq+1
    return sum_n"""


def sum_of_n_range(n):
    sum_n=0
    prev=0
    t=1
    for i in range (1,n+1):
        if i%2==0:
            sum_n=sum_n+(prev+1)
        else:
            prev=3*(t-1)+1
            sum_n=sum_n+prev
            t=t+1
    return sum_n
if __name__ == "__main__":
        max_n = int(input("Enter a value of n:"))
        series_sum_range = sum_of_n_range(max_n)
        """series_sum_while=sum_of_n(max_n)
        print(series_sum_while)"""
        print(series_sum_range)