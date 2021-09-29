mystring = '       Hello          '
#to remove spaces from both the ends use strip(), to remove spaces from left side use lstrip(),rstrip()for right
print(mystring.strip())
#this is not inplace
#i.e you've to assign the output to another variable
my = mystring.strip()
print(my)

#to find the index of a character
string = "Hi HEllo Welcome"
print(string.find('H'))
print(string.find("Ello"))
print(string.find("N"))
print("Number of occurences of H ",string.count("H"))
print("Number of occurences of Z ",string.count("Z"))

#if we want to replace a character we can use replace()
mys = string.replace("HEllo",'Nivedha')
#here if old value i.e "HEllo" doesn't exist,the string is printed without any error and without any replacement 
print(mys)
print(string)

#split() splits the given string into list of words based on a delimiter
string1 = "Hi How are you doing!"
li = string1.split() #space is the default delimiter
print(li)
#use join method to join the split elements
string2 = " ".join(li)
print(string2)


#format method
var =3.127368927927
print("The greeting is {} and {:.2f}".format(string1,var))

#use f strings
print(f"The greeting is {string2} and {var}")