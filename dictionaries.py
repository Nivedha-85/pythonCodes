my_dict={"name":"Mark","age":28,"college":"RNSIT"}
#print(my_dict)

#use dict() but no need to explicitly specify quotes for key and use '=' for assigning value to the key
my_dict1=dict(name="Nivedha",age=21,college="RNSIT")
#print(my_dict1)

''' del my_dict["name"]
my_dict1.pop("age")
print(my_dict1)
my_dict.popitem() #removes the last key value pair
print(my_dict) '''

for key in my_dict: # or my_dict.keys()
    print(key)
for value in my_dict.values():
    print(value)


for item in my_dict.items(): #o/p: tuple of values
    print(item)

'''
o/p: ('name', 'Mark')
('age', 28)
('college', 'RNSIT')
'''

for key,val in my_dict.items():
    print(key,val)

#for copying
#here by doing this copy , any change made in either of them will reflect the other because they point to the same memory address
my_dict2 = my_dict
print(my_dict2)
my_dict2["Email"] = "nivedham2000@gmail.com"
print(my_dict)
print(my_dict2)

#to not reflect change in the other
my_dict3 = my_dict.copy()
my_dict3["Father's name"] = 'xyz'
print(my_dict)
print(my_dict3)

#another method to copy without reflecting change in the other
my_dict3 = dict(my_dict) #argument is the dictionary that we need to copy
my_dict3["Father's Name"] = 'xyz'
my_dict3["Mother's Name"] = "mno"
print(my_dict)
print(my_dict3)

#to update an existing dictionary with a key value pair of another dictionary
my_dict.update(my_dict3)
print(my_dict)
