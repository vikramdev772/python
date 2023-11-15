"""
        Ways to define a function 

        1) Takes Nothing , Returns Nothing 
        2) Take Something , Returns Nothing 
        3) Takes Nothing , Return Something 
        4) Takes something , Return Something 

"""
print("\n\t Takes Nothing \n")
def add():
    print("\n\t Enter two numbers : ")
    a=int(input())
    b=int(input())
    c=a+b
    print("\n\t Sum : ",c)

add()
print("\n\t Returns Nothing \n")
# print(n)  nameError n is not defined it printing outside the def function 

#       Enter two numbers :
# 4
# 5

#          Sum :  9


"""
        Scope  Variable 
        2types
        Local , Global
        in python sub kuch Global varibale 
    The varibles are used inside the function are the local variable so it is local scope 



"""

print("\n\t Take something \n")
def sum(a,b):  #Formal Arguments 
    c=a+b
    print("\n\t sum : ",c)

print("\n\t Returns Nothing \n")
sum(10,5)   #Actual Arguments 




#  Take something


#          Returns Nothing


#          sum :  15



