'''
print("Enter three numbers");
a = input('a ');
b = input('b ');
c = input('c ');
small = a;
if( b<a and b<c ):
    small = b;
elif( c<a and c<b):
    small = c;
else:
    small = a;
print("Smallest:",small);
'''


# add and multiply two complex numbers
'''
a = input("Complex no 1")
b = input("Complex no 2")
c = complex(a) + complex(b)
d = complex(a) * complex(b)
print(c);
print(d)
'''


'''
myage = input("Enter age");
print("You will be " +str(int(myage)+1)+ " in a year")
'''


#print("I am " + str(20) + " years old")

#add two numbers
'''
num1 = input("enter number 1")
num2 = input("enter number 2")
num3 = int(num1) + int(num2)
print(num3)
'''


#print("dog" != 'cat')
#print(not True)

'''
i = 10
while(i>0):
    print("India")
    i = i-1
'''

'''
i = 'india'
for j in i:
    print((j))
'''

#area of rectangle
'''
l = input("Enter the length\n")
b = input("Enter the breadth\n")
print("Area of the rectangle is:",int(l)*int(b))
'''

#area of the triangle
'''
b = input("Enter the base\n")
h = input("Enter the height\n")
print("Area of the triangle is:",(int(b)*int(h))/2)
'''

#area of cube = 6a^2
'''
a = input("Enter the side of the cube\n")
print("Area of the cube is:",int(a)*int(a)*6)
'''

#even number series
'''
for i in range(0,100,2):
    print(i)
'''

#no.s in decreasing order from 100 to 0
'''
for i in range(100,0,-1):
    print(i)
'''

#odd number series
'''
for i in range(1,100):
    if(i%2 == 1):
        print(i)
'''

#prime numbers upto 100
'''
for i in range(1,100):
    if(i%i == 0 and i%1 == 0):
        print(i)
'''


#print("Alice" + "Bob");
#print('Alice '*5)

'''
print('Hello World!')
print("Your good name please?")
myName = input()
print("Welcome,",myName+"!")
print("The length of your name is:",len(myName))
print("Your age?")
myAge = input()
print("Cool!\nYou will be "+ str(int(myAge) +1) + " in a year")
'''

#print(len(" "))


'''
spam = 0
while(spam < 5):
    print(spam)
    spam = spam +1
'''



'''
name = ' '
while( name != 'your name'):
    print("Please enter your name")
    name = input()
print("Thank You!")
'''

'''
while True:
    print("Please enter your name")
    name = input()
    if( name == 'your name'):
        break
print("Thank You!")
'''


'''
for x in range(2,30,3):
    print(x)
'''

'''
for x in range(5,-1,-1):
    print(x)
'''

'''
import random
for i in range(5):
    print(random.randint(1, 10))
'''

'''
import sys
while True:
    print("type exit to exit")
    response = input()
    if(response == 'exit'):
        sys.exit()
print("You typed"+'response.')
'''

'''
def hello(name):
    print("Hello",name)
hello('Alice')
hello("Bob")
'''

'''
print("Hello",end=' ')
print("World!")
'''

#print("dogs",'cats','cows','crows',sep=',')
#print("dogs",'cats','cows','crows')

'''
def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
spam()
'''

#guess the secret number
'''
import random
secretNumber = random.randint(1,20)
print("I am thinking of a number betweeen 1 and 20")

for guessesTaken in range(1,7):
    print("Take a guess")
    guess = int(input())
    if(guess < secretNumber):
        print("The number you guessed is lower than the secret number")
    elif(guess > secretNumber):
        print("The number you guessed is higher than the secret number")
    else:
        break
if(guess == secretNumber):
    print("Good job! You guessed my secret number in " +str(guessesTaken)+" guesses")
else:
    print("Bad Luck!The number that I was thinking of was"+str(secretNumber))
'''


#Arithmetic operations 
'''
num1 = input("Enter the first number")
num2 = input("Enter the second number")
num3 = input("Enter the third number")
sum = int(num1) + int(num2) + int(num3)
sum1 = float(num1) + float(num2)
#print(sum)
#print(sum1)

min = float(num1) - float(num2)
#print(min)

mul = int(num1) * int(num2)
#print(mul)

div = int(num1) / int(num2)
#print(div)

print('The sum of {0} and {1} and {2} is {3}'.format(num1,num2,num3,sum))
print('The difference of {0} and {1} is {2}'.format(num1,num2,min))
print('The product of {0} and {1} is {2}'.format(num1,num2,mul))
print('The quotient of {0} and {1} is {2}'.format(num1,num2,div))
'''

#to solve ax^2 + bx + c
'''
import cmath

a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

d = (b**2)-4*a*c

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print("The solutions are:{0} and {1}".format(sol1,sol2))
'''
#to swap two numbers
'''
a = input("Enter the first number")
b = input("Enter the second number")
temp = a;
a = b;
b = temp;
print("The values of a and b after swapping are:{} and {}".format(a,b))
'''

'''
str = 'Python'
for i in str:
    print(i)
'''


'''
for i in range(1,10):
    #print(i)
    print(i,end=' ')
'''

#to print the table of the given number
'''
n = int(input("enter the value of n"))
for i in range(1,11):
    c = i * n
    #print(int(n)+" * "+int(i)+ " = "+int(c))
    print('{} * {} = {}'.format(n,i,c))
'''

'''
list = ['Rhea','Neha','Nidhi','Nivedha']
for i in range(len(list)):
    print("Hello!",list[i])
'''


#pattern
'''
rows = int(input("Enter the rows"))
for i in range(0,rows+1):
    for j in range(i):
        print('*',end=' ')
    print()
'''

'''
for i in range(0,5):
    print(i)
    break
else:
    print("For loop is exhausted")
print("The loop is broken due to the break statement.....came out of the loop")
'''

'''
import math
num = math.pow(10,10)
print("The number of number is",num)
'''

#pass
'''
for i in [1,2,3,4,5]:
    if(i==4):
        pass
        print("This is pass block")
    print(i)
'''


#function
'''
def sum():
    a = 10
    b = 20
    c = 30
    return a+b+c
print("The sum is:",sum())
'''

'''
def func(name,message):
    name = 'Rhea'
    message = 'hi'
    print("Printing the message with",name,"and",message)
func('Nivedha',"Hello")
'''


'''
def si(p,t,r):
    return p*t*r/100
print("Simple Interest is:",si(t=10,r=5,p=9000))
'''


'''
ls1 = ['Nivedha','Rhea','Nam','Sahana','Sonal']
print(len(ls1))
print(type(ls1))
print(ls1)
ls2 = [1,2,3]
print(ls2)
ls3 = [1,'NiM',['Rhea',1,2.3]]
print(len(ls3))
print(ls3[2][0])
print(ls3[2][-3])
print(ls1[:2])
'''


'''
ls1 = ['cat','bat','rat','sat','tat']
ls2 = ['N','r','n','R','S']
print(ls1 + ls2)
print(ls1 * 2,ls2 * 2)
'''


'''
ls = ['Nivedha','mibz','Janani','Hadii']
print(ls)
del ls[3]
print('After deleting',ls)
'''


'''
favFruits = []
while True:
    print('Enter the name of fruit ' + str(len(favFruits) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    favFruits = favFruits + [name] # list concatenation
print('Your Favorite Fruits are:')
for name in favFruits:
    print(' ' + name)
'''



'''
def spam():
    eggs = 99;
    print(eggs)
eggs = 100
spam()
print(eggs)
'''


'''
ls = ['hi','Hello','Hey']

print("hi" in ls)
print('Howdy' in ls)
for i in ls:
    print(i)

ls.append('Hola')
print(ls)
ls.insert(0,1)
print(ls)
'''

''''
catNames=[]
while True:
    print("Enter the name of the cat " + str((len(catNames))+1)+" or enter nothing to stop.")
    name = input()
    if name == ' ':
        break
    catNames = catNames+[name];
print("The cats in the list are:")
for i in range(len(catNames)):    #for i in catNames:
    print(catNames[i])            # print(i)
'''


'''
myPets = ['Duke','Enzo','Dunzo','Ros']
#print("Enter the name of pet")
name = input("Enter the name of the cat\n")
if name in myPets:
    print("Yay! That's my pet")
     
else:
    print("Aye! No,That's not my pet")
'''

'''
myPets = ['Duke','Enzo','Dunzo','Ros']
name = myPets[0]
name1 = myPets[1]
name2 = myPets[2]
name,name1,name2 = 'NiM','RAB','NAM'
print(name)
for i in myPets:
    print(i)
print(name2)
'''


'''
animals = ['Ele','Lion','Tiger','Cheetah']
for index,key in enumerate(animals):
    print(index,key)
'''


'''
import random
Birds = ['Peacock','Parrot','Pigeon','Crow']
print(random.choice(Birds))
print(Birds)

del Birds[0]
print(Birds)

Birds.remove('Crow')
print(Birds)

Birds.clear()
print(Birds)

del Birds
print(Birds)
'''

'''
Birds = ['Peacock','Parrot','Peacock','Pigeon','Crow']
Birds.remove('Peacock')
Birds.sort(reverse = True)
print(Birds)
'''

'''
p = ['Animal','ant','Bear','bat','carol','Cat']
p.sort()       #sorts in ASCIIbetical order not alphabetical order
print(p)
'''



'''
import random
ls = ['Alice','Bob','Carol','David']
random.shuffle(ls)
print('Shuffled list is',ls)
print('Random choice '+random.choice(ls))
'''


'''
ls = ['length','length','Breadth','Height']
print(ls.index('length'))
'''

'''
import operator
from _operator import eq
ls = [1,2,3,4,5]
ls1 = [6,7,8,9,10]
print(eq(ls,ls1))
'''

'''
ls = [1,2,3,4,5]
print(max(ls))
print(min(ls))
'''

'''
spam = [1,2,3,4,5]
cheese = spam
print(spam)
print(cheese)
cheese[0] = 10
spam[1] = 9
print(spam)
print(cheese)
'''


'''
def eggs(someParameter):
    someParameter.append('Hello')
param = [1,2,3,4,5]
eggs(param)
print(param)
'''




'''
tp = (1,2,3,4,5)
for i in tp:
    print(i)
'''

'''
tuple = ('abc',1,2,'xyz')
tu1 = (' def',3,4,5)
tuple = tuple + tu1
print(tuple)
del tuple
print(tuple)
'''

'''
tuple = ('hi') 
print(tuple[0:1] )
'''



'''
dict = {'Name' : 'Nivedha','Age': 20}
dict1 = {'Name' : 'Nim', 'Age' : 10}
print(dict.keys())
print(dict.values())
dict['Name'] = dict1['Name']
print(dict)
del dict['Name']
print(dict)
dict.clear()
print(dict)
del dict1
print(dict1)
'''

'''
dict = {'Class' : 'fifth','Section': 'B','Class' : 'Sixth'}
print(dict)
'''


'''
import copy
spam = [1,2,3,4,5]
spam1 = copy.copy(spam)
print(spam)
print(spam1)
spam[1] = 10
print(spam,spam1)
spam.append([4,4,4])
print(spam)
print(spam1)
spam1 = copy.deepcopy(spam)
spam[0][1] = 5
print(spam)
'''


'''
from array import *
array1 = array('i',[1,2,3,4,5])
for x in array1:
    print(x)
array1.insert(1,60)
for x in array1:
    print(x)
'''

'''
import random

print(random.randrange(1,10))
'''


#String methods
'''
string = 'HEllO'
print(string[-5:-3])
string1 = " Hello, world"
print(string1.strip())
print(string1.upper())
print(string1.lower())
print(string1.replace("H","G"))
print(string1.split(","))
'''


'''
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
print( "ain" not in txt)
'''


'''
string = "NIVEDHA is NIVEDHA"
print(string.capitalize())
print(string.casefold())
print(string.center(80,'*'))
print(string.count("NIVEDHA"))
print(string.endswith("A"))
print(string.find("A"))
print(string.index("A"))
print(string.swapcase())
'''

#print(bool([]))

'''
t = [('a','b'),('c','d')]
for i,j in t:
    print(i,j)
'''


'''
t = (1,2,3,4,4,5,5,5,5,53,3,3,2,2)
t1 = ("Hello")
print(t.count(5))
print(t.index(5))
print(type(t))
print(type((t1,)))
print(t1)
'''


'''
t1 = [1,2,3,4,5]
print(tuple(t1))

t = ('a','b','c','d','e')
print(list(t))

print(list("Hello"))
print(tuple("Hello"))
'''

'''
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
'''





'''
di = {"Name" : "Alice", "Age" : 35, "Country": "Ame"}
print(di.get("Colour",0))
print(len(di))
di.pop("Name")
print(di)
del di["Age"]
print(di)
di.clear()
print(di)
di.remove()
print(di)
'''


'''
class p:
    x = 10
p1 = p()
print(p1.x)
'''



'''
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(oelf):           #self is not mandatory.you can name anything of ur own
        print("My name is",oelf.name)

p = person("Nivedha",20)
print(p.name)
print(p.age)
p.myfunc()
del p
print(p.name)
'''


'''
class person:
    def __init__(self,fname,lname,age):
        self.FirstName = fname
        self.LastName = lname
        self.age = age
    def printname(self):
        print(self.FirstName,self.LastName,self.age,)
class Student(person):
    pass
p = person("Nivedha","M",20)
p.printname()
p = Student("Niv","M",20)
p.printname()
'''

'''
spam = [2,4,6,8,10]
spam[2] = 'hello'
print(spam)
'''


'''
spam = ['a','b','c','d']
print(spam[int(int('3'*2) / 11)])
print(spam[-1])
print(spam[:2])
'''

'''
bacon = [3.14,'cat',11,'cat',True]
print(bacon.index('cat'))
bacon.append(99)
print(bacon)
(bacon.remove('cat'))
print(bacon)
'''


'''
list = [1,2,3]
list.append([5,6])
print(list)
list.insert(0,8)
print(list)
del list[0]
print(list)
list.remove(2)
print(list)

list.pop(2)
print(list)
'''

'''
class Point:
    def __init__ (self,a=0,b=0):
        self.x=a
        self.y=b
    def __add__ (self, p2):
        p3=Point()
        p3.x=self.x+p2.x
        p3.y=self.y+p2.y
        return p3
    def __str__ (self):
        return "(%d,%d)"%(self.x, self.y)

p1=Point(10,20)
p2=Point(4,5)
print("P1 is:",p1)
print("P2 is:",p2)
p4=p1+p2 #call for add () method
vars(p4)
print("Sum is:",p4)


t1 = {'data': 60}
del t1
print(t1)
'''


'''import os
print(os.getcwd());
print(os.path.abspath('./Python_Programs'));
print(os.path.isabs('./Python_Programs'));
print(os.path.relpath('Python_Programs'));
print(os.path.isdir('/home/nivedha/Python_Programs'));
print(os.path.dirname('/home/nivedha/Python_Programs'));
print(os.path.basename('/home/nivedha/Python_Programs'));
'''



'''
class partyanimal:
    x=0
    def __init__(self,name):
        self.name = name
        print(self.name,'constructed')

    def party(self):
        self.x = self.x+1
        print(self.name,'party count',self.x)

s = partyanimal('Sally')
j = partyanimal('Jacob')
s.party()
j.party()
s.party()
'''


'''
class a:
    def __init__(self,name='YUM'):
        self.name = name 
        print(self.name,'created')
    
    def __del__(self):
        print(self.name,"object destroyed")

a1 = a()
b1 = a("RAB");
print("Deletion of first object")
print("Deletion of second object")
'''



'''

class base1:
    def show(self):
        print("Show method of base class 1")
class base2:
    def show(self):
        print("Show method of base class2")
class derived(base1,base2):
    def childshow(self):
        print("Show method in derived class")
b = base1()
b.show()
bb = base2()
bb.show()
c = derived()
c.childshow()
'''

Q = input()
s = ""
#t = []
for i in range(int(Q)):
    var = input().strip().split(' ')
    if(var ==1):
        s1 = input()
        s+=s1
        t = list(s.split())
    elif(var==2):
        n = input()
        for k in range(int(n)):
            t.pop()
    elif(var ==3):
        pos = int(input())
        print(t[pos])
    else:
        print(s)
    
            
        

