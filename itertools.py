from itertools import product
# here the product is cartesian product
a=[1,2]
b=[3,4]
print("Cartesian Product")
prod = product(a,b)
print(list(prod))

from itertools import permutations
a=[1,2,3]
perm=permutations(a)
print("Permutations")
print(list(perm))

#if we want the permuatations to be length of two
perm1 = permutations(a,2)
print(list(perm1))

#perform combination
from itertools import combinations
print("Combinations")
a=[1,2,3,4]
comb=combinations(a,2) # if (1,2) is given (2,1) will not be given
print(list(comb))


''' #to overcome the above problem use combinations with replacement
from itertools import combinations_with_replacememt
print("combinations with replacement")
a1=[12,3,4,5]
comb1=combinations_with_replacememt(a1,2)
print(list(comb1)) '''
#accumulate.
from itertools import accumulate
b=[1,2,2,3]
print("Accumulate")
acc=accumulate(b)
print(list(acc))

#from itertools count,cycle,repeat


