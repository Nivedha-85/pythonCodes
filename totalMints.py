'''
n will be given that is the number of mints with first person and calculate the total mints according to the
condition that says each person will have sum of the mints with previous people minus 1.
find the total mints
'''
n=(input("Input n for number of mints with first person"))
q=input("Number of people in the queue ")
prev=int(n)
sum1= int(n)
for i in range(1,int(q)):
    prev=sum1-1
    sum1+=prev
print(sum1)