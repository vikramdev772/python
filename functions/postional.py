
# def s(a,b,e,d):
#     c=a+b
#     return c

# print("\n\t Sum : ",s(2,3))
# print("\n\t Sum : ",s(2,3,4))
# print("\n\t Sum : ",s(2,3,4,5))

# TypeError: s() missing 2 required positional arguments: 'e' and 'd'
"""
            Default Arguments 

    Default value indicate that the funciton 
    argument will take that value if no argument value is passed during the 
    function call.

    The default value is assigned by using the assignment (=)
    operator.

"""

def s(a,b,e=1,d=0):
    c=a+b+e+d
    return c

print("\n\t Sum : ",s(2,3))
print("\n\t Sum : ",s(2,3,4))
print("\n\t Sum : ",s(2,3,4,5))

# Sum :  6

#          Sum :  9

#          Sum :  14


# Default value consider hotha hi 




# syntax error compile time error 


print("\n\t Return something \n")
def f1():
    print(" \n\t hello ")
a=f1()
print("\n\t return :  ",a," keyword (true , false , none )")


# Return something


#          hello

#          return :   None  keyword (true , false , none )


print("\n\t a = ",a,type(a))
# a =  None <class 'NoneType'>


"""
        Posional vs keyword Argument 

"""

def f(x,y):
    print("\n\t x : ",x," y : ",y)

f(4,6)
print("\n\t  4,6 are called positional arguments \n")

#  x :  4  y :  6

#           4,6 are called positional arguments


# Here f(x,y) x and y are formal arguments 

r=f(y=9,x=8)

print("\n\t Keyword  Arguments  : ",r)


#  x :  8  y :  9

#          Keyword  Arguments  :  None


