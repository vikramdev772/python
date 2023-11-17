"""
            Mutability and hashability

    Mutable objects are changable 
    immutable objects are changable 
    All immutable objects are hashable but not all hashable object are imutable
    Hashable is a feature of python ibjects that tells if the object has a hash value
    or not , If it has a hash value that does not change during its entire life time.


    int,float,complex,bool,str,tuple   are  hashable

    list , set, dict   are mutable  (not hashable )

"""

z=4.5
print(hash(z))

# 1152921504606846980

print("\n\t str \n")

""" str is a class 
    str is imutable 
    str is iterable
    str is hashable
    str is a sequence 
"""

print("\n\t Enter some numbers : ",end="")

l=eval(input())
print(l)
     


#          Enter some numbers : 4-3
# 1



""" Acessing str elements 

    s1[index]
    print(s1)
    for loop
    slicing operator

"""


