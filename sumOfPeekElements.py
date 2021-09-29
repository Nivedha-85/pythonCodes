"""
given array [13,5,14,12,8,30,15]
peek elements are [13,14,30] and the sum is 57
13 because 13 > 5
14 because 14 > 5 and 14 >12
30 because 30>8 and 30 > 15
"""
li=[]
def peek_elem(arr):
    if arr[0]>arr[1]:
        li.append(arr[0])
    if arr[len(arr)-1] > arr[len(arr)-2]:
        li.append(arr[len(arr)-1])
    for i in range(1,len(arr)-1):
        if(arr[i]>arr[i-1]) and (arr[i]>arr[i+1]):
            li.append(arr[i])
    return sum(li)

n=int(input("Enter the array elements"))
print("Enter the elements")
arr=list(map(int,input().split()))
print(peek_elem(arr))