""" 
        Lambada Expression

"""

print("\n\t lambda expression \n")

# lambda is a keyword 
# lambda expression are syntactically
# restricted to a single expression 

# lambda input : expression
# lambda a,b : a+b

# no need of def keyword 


# we can define a function without a name ( Anonymous function )

# lambda : print("\n\t Hello \n")


# lambda a,b:a+b // args are directly 

# def add(a,b): args 
#     return a+b  add,add() 
# print()


# Function object

x=int(input("\n\t Enter a num1 : "))
y=int(input("\n\t Enter a num2 : "))
s=lambda a,b:a+b
print("\n\t Sum : ",s(x,y))



# lambda expression


#          Enter a num1 : 5

#          Enter a num2 : 4

#          Sum :  9


"""name=(lambda expresion function object )"""


print("\n\t diffrence of b-a : ",(lambda a,b:b-a)(5,14))
    # diffrence of b-a :  9


    