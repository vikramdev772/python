
"""
        What are iterables ?

    An iterable object is something that contains a countbale number of values.

    you can travers through all the values from begining to the end.

    Technically , in python, an iterator is an object , which implements the 
    iterator proctocal, which consist of methods _ _ iter _ _ () 
    and  _ _next _ _ ()

"""


"""
        Various iterables

        .range
        .list
        .tuple
        .str
        .bytes
        .bytearray 
        set
        .frozenset
        .dict 

"""


"""  
            range

    .range is a class
    .range is immutable sequence  (immutable means not changeable)
    .range can contain only int type values
    .range contains sequence of integers with common difference (Arithmetic Progrssion)


"""

"""
        How to create range Object ?

    r = range (beg:end:step)

    example

            range(1,10,1) 123456789
            1-inclusive 10-Exclusive 1-common gap
            range(2,8,2)  2 4 6
            range(10,3,-2) 10 8 6 4

        
        """
"""
    1) rabge(end)    beging value beg= 0  step=1
    2)range(beg,end)   step = 1
    range(1,5,-2) ==> empty range object 


"""

r1=range(2,10,2)
print(r1)
# range(2, 10, 2)
for i in r1:
    print(i,end=' ')

# 2 4 6 8
for a in range(-10):
    print(a)
print("\n\t empty range object \n")