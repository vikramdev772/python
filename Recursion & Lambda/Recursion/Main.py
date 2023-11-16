
print("\n\t Recursion \n")
print("\n\t Function calling itself it called recursion \n")

# def f1():
#     print("\n\t Recursion  ")
#     f1()




print("\n\t Recursion tree \n")


def f1(n):
    if n==1:
        return 1;
    s=n+f1(n-1)
    return s

r=f1(3)
print("\n\t  ans : ",r)

# Recursion tree 


# 	  ans :  6

print("\n\t Factorial program \n")
x=5
def fact(n):
    if n==1:
        return 1
    f=n*fact(n-1)
    return f

ans=fact(x)
print(f"\n\t factorial of {x} : ",ans)


	#  Factorial program 


	#  factorial of 5 :  120

"""
    n>1 n+f1(n-1)
    n=1 1

    f1(5)

        => 5+f1(4)
        => 5+4+f1(3)
        => 5+4+3+f1(2)
        => 5+4+3+2+f1(1)
        => 5+4+3+2+1

"""



# In recursion , problem is solved in terms of problem itself

# Each time recursive function call to itself for little simpler version of the original problem 


