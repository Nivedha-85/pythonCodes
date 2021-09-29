myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)
# if element isnt found key error will be generated
#myset.remove(4)
#use discard to overcome this
myset.discard(4)
print(myset)

#to clear all the elements
#myset.clear()
myset.pop()
print(myset)

#union- combines elements from the sets mentioned without eliminationg any
odd={1,3,5,7,9,2,3}
even={0,2,4,6,8}
print(odd.union(even))
#intersection-gives the common element/s
print(odd.intersection(even))
#difference A-B(here odd-even) ,elements of A which are not in B
print(odd.difference(even))
#differenc B-A(even-odd),elements of B which are not in A
print(even.difference(odd))
#symmetric difference gives all elements except common elements
print(even.symmetric_difference(odd))


#all these fucntions i.e union,intersection etc doesn't modify the original set 



#-------------------------------------------------------------------------------------------------
#to modify the set in place
#odd.update(even)
print(odd)
#print(odd.intersection_update(even))
print(odd.issubset(even))