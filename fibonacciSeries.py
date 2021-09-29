n=int(input("Enter the number of terms:"))
n0,n1=0,1
count=0
fib=[]
if(n<=0):
    print("Enter a positive integer please")
elif(n==1):
    print(n0)
else:
    while(count<n):
        print(n0)
        fib.append(n0)
        nth = n0+n1
        n0=n1
        n1=nth
        count+=1
print(fib[len(fib)-1])