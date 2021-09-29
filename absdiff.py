def count(arr,n,num,diff):
    cnt=0
    for i in range(n):
        if(abs(arr[i]-num)) <= diff:
            cnt+=1
        if cnt:
            return cnt
    return -1
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
num = int(input())
diff= int(input())
print(count(arr,n,num,diff))