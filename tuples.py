
import sys
#parenthesis is optional
my_tuple = "Max",28,"RNSIT" #=>my_tuple=("Max",28,"RNSIT")
my_list=["Max",28,"RNSIT"]
name,age,college = my_tuple
print(name,age,college)
print(sys.getsizeof(my_tuple))
print(sys.getsizeof(my_list))
