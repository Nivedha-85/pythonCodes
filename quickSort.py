ele = [8,7,5,3,4,2,10,0]
l = ele[0]
h = len(ele)-1
def partition(ele,l,h):
    pivot = ele[0]
    i,j = l,h
    while(i<j):
        while(ele[i]>=pivot):
            i=i+1
        while(ele[i]<=pivot):
            j=j-1
        if(i<j):
            ele[i],ele[j] = ele[j],ele[i]
    pivot,ele[j] = ele[j],pivot
    return j
def quickSort(ele,l,h):
    j = partition(ele,l,h)
    quickSort(ele,l,j)
    quickSort(ele,j+1,h)
quickSort(ele,l,h)
        
    
