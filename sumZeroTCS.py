import sys
n = int(input("Enter the number of elements"))
arr =[]
sum = 0
for i in range(n):
    arr.append(int(input("Enter the element ")))
for j in range(n):
    for k in range(j+1,n):
        sum = sum+arr[k]
        if(sum == 0):
            print("1")
            break

print(arr)
