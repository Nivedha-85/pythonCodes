'''
find the missing number until the given n value
'''
import time
def missing(array,n):
    start_time=time.time()
    num=0
    for i in range(1,n+1):
        if(i not in array):
            num=i
    end_time = time.time()
    print(start_time-end_time)
    return num

n=int(input("Enter the range"))
arr=[]
n1=int(input("Enter the number of elements in array"))
for i in range(n1):
    arr.append(int(input()))

print("The missing element is:",missing(arr,n))