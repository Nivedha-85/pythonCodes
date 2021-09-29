'''
The function accepts an integers sum and an integer array arr of size n. Implement the function to find the pair, (arr[j], arr[k]) where j!=k, Such that arr[j] and arr[k] are the least two elements of array (arr[j] + arr[k] <= sum) and return the product of element of this pair

NOTE

    Return -1 if array is empty or if n<2
    Return 0, if no such pairs found
    All computed values lie within integer range'''
def pair(arr,sum1):
    if(len(arr)==0 or len(arr)<2):
        return 0
    arr1 = sorted(arr)
    if(arr1[0]+arr1[1]<=sum1):
        return arr1[0]*arr1[1]
    elif(arr1[0]+arr1[1]>sum1):
        return 0
    

n=int(input())
arr=list(map(int,input().split()))
sum1=int(input())
print(pair(arr,sum1))