

""" 
set introduction

set is a class
set is mutable
set is not hashtable
set is iteratable

set is not a sequence  (order is not preserved )
set cannot have duplicate values

indexing is not applicable to set object
(-ve,+ve indexing no)

slicing operator is not applicable 
set doesn't guarantee to store values in the order of insertion 


"""


s1={1,5,8}
print(s1)
print(type(s1))
# {8, 1, 5}
# <class 'set'>

s2={2,3,1,6,9,1,4,8,3,4}
print(s2)

# {1, 2, 3, 4, 6, 8, 9}


s3={}
print("\n\t not empty set it is ",type(s3))

#  not empty set it is  <class 'dict'>


s4=set()
print("\n\t Empty set : ",type(s4))  #'int' object is not iterable
#   Empty set :  <class 'set'>

# s5=set(10)
# print(s5)

s5=set([10,7,20,3])
print(s5)

# {10, 3, 20, 7}


l1=[20,10,12,20,20,30,10,5,12,11]
print(l1)
l1=list(set(l1))
print(l1)

