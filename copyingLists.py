''' list_original=['apple','banana','mango']
list_copy=list_original
list_copy.append("Orange")
print(list_original)
print(list_copy)
 '''
#so here any changes made to any list is getting affected in the other

''' list_original=['apple','banana','mango']
list_copy = list_original.copy()
list_copy.append("Ant")
print(list_original)
print(list_copy) '''
# here any change made in either of the lists doesn't modify the other

list_original=['apple','banana','mango']
list_copy = list(list_original)
list_copy.append("Ant")
print(list_original)
print(list_copy) 

