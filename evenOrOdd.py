'''The function accepts an integers arr of size ’length’ as its arguments you are required 
to return the sum of second largest largest element from the even positions and second smallest 
from the odd position of given ‘arr’

Assumption:

    All array elements are unique
    Treat the 0th position a seven

NOTE

    Return 0 if array is empty
    Return 0, if array length is 3 or less than 3
    '''

def sums(arr):
    even_arr=[]
    odd_arr=[]
    if len(arr) ==0 or len(arr)<=3 :
        return 0
    for i in range(len(arr)):
        if(i%2==0):
            even_arr.append(arr[i])
        else:
            odd_arr.append(arr[i])
    even_arr=sorted(even_arr)
    odd_arr=sorted(odd_arr)
    print(even_arr[len(even_arr)-2]+odd_arr[1])


n=int(input())
arr=list(map(int,input().split()))
sums(arr)



