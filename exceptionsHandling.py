marks=50
a=[1,2,3]
try:
    a=5/0
    print(a)
except Exception as e:
    print(e)

try:
    print(a[4])
    b=marks/0
    print(b)
    #print(c)
except IndexError:
    print("oops! index out of range")
except ZeroDivisionError:
    print("Divide by zero error")
except NameError:
    print("name error")
finally:
    print("hi! I am finally keyword..i always get executed")

b=-5
if b<0:
    raise Exception("b should be positive")


'''
utmost one except gets executed
finally gets always executed irrespective of exception being raised or not
'''

#to define our own exception
class valueTooHighError(Exception):
    pass
def test_value(x):
    if x>100 :
        valueTooHighError("Value too high for life")
test_value(1000)
