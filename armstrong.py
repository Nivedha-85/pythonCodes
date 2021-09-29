'''
armstrong number
ex: 153
1^3+5^3+3^3=153
i.e sum of individual digits' cube is equal to the number
'''

n=int(input('Enter the number'))
sum1=0
temp=n
while(temp!=0):
    rem= temp%10
    sum1+=rem ** 3
    temp//=10
if(sum1==n):
    print(n,"Is an armstrong number")
else:
    print(n,"Is not an armstrong number")