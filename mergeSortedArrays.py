""" '''
merge two sorted arrays without using any extra space..
'''

import time
start_time=time.time()
array2=[1,3,5,7]
array1=[0,2,6,8,9]
for i in range(len(array1)):
    minimum = min(array2)
    index1 = array2.index(minimum)
    if(array1[i]>array2[index1]):
        array1[i],array2[index1]=array2[index1],array1[i]
print(array1)
print(sorted(array2))
end_time=time.time()
print(start_time-end_time) """

import time
def merge(x,y):
    m=len(x)
    n=len(y)
    for i in range(m):
        if(x[i]>y[0]):
            temp=x[i]
            x[i]=y[0]
            y[0]=temp
            first=y[0]
            k=1
            while(k<n and y[k]<first):
                y[k-1]=y[k]
                k+=1
            y[k-1] = first
x=[1,4,7,8,9]
y=[3,4,2]
start_time=time.time()
merge(x,y)
print(x)
print(y)
end_time=time.time()
print(start_time-end_time)