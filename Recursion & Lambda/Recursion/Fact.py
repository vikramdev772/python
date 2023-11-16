print("\n\t Factorial program \n")
x = 5
print("  factorial of  ",str(x)," is  1*",end="")

def fact(n):
    if n == 1:
        return 1
    f = n * fact(n - 1)
    print(n, end="")
    if n > 1:
        print("*", end="")
    return f

ans = fact(x)
print(f" : {ans}")


# 	 Factorial program 

#   factorial of   5  is  1*2*3*4*5* : 120