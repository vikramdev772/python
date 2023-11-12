""" a=5  => int 
    b='5' => str
    a+b int + str Error
    a+int(b)
    int+int  No error    
"""

a=6
b="4"
c=a+int(b)
print(c)    #10


x=3
y=3.14
z=x+int(y)
print("\n\t Type conversion to float to int : "+str(z))
# Type conversion to float to int : 6
v=float(x)+y
print("\n\t Type conversion int to float : "+str(v))
#  Type conversion int to float : 6.140000000000001



s="8.5"
i=float(s)
integer=int(i)+5


print(integer) #13


