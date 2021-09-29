#to define our own exception
''' class valueTooHighError(Exception):
    pass
def test_value(x):
    if x>100 :
        raise valueTooHighError("Value too high for life!json.py")
test_value(1000)
 '''

a=[1,2,3,5,6]
beginning,*middle,end=a
print(beginning)
print(middle)
print(end)