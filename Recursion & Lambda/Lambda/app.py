

print("\n\t Recursion using lambda \n")

# Calculate factorial of a number using recursive lambda expression

f=lambda a:1 if a==0 else a*f(a-1)
n=5
print(f"\n\t factorial of {n} : ",f(n))

#   Recursion using lambda 


#          factorial of 5 :  120


# f=lamdba a:a*f(n-1)

# base case :  a ki value 1 then the result should be one  ( a:1 if a==0) if the condition is true return a:1 




