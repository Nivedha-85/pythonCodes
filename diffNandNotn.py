def diff(n,m):
    sum_divisible=0
    sum_not=0
    i=1
    while(i <=m):
        if(i%n == 0):
            sum_divisible+=i
        else:
            sum_not+=i
        i+=1
    return(sum_not-sum_divisible)

n=int(input())
m=int(input())
print(diff(n,m))