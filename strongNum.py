"""
A number is said to be a strong number if the factorial of its individual digits is equal to the number
ex: 1!+4!+5!=145 is a strong number
"""

def strongNum(number):
    sum1=0
    for i in number:
        #print(i)
        s=strNum(int(i))
        sum1+=s
    return sum1
def strNum(num):
    #print(num)
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

number=input()
sum1=(strongNum(number))
print("the number is:",int(number))
print("The sum of factorial of each digit is ",sum1)
if(int(number)==sum1):
    print("Yes,The number is strong number")
else:
    print("No")