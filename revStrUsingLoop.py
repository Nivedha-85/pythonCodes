string=input("Enter the string")
string1=''
l=list(string)
i=0
j=len(string)-1
while(i<j):
    l[i],l[j]=l[j],l[i]
    i+=1
    j-=1
for i in range(len(l)):
    string1+=l[i]
print(string1)

'''
without using loop:

string = "Nivedha"
print(string[::-1])
'''