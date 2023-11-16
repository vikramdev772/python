
def SquareSum(n):
    if(n==1):
        return 1
    s=n*n+SquareSum(n-1) # n**2+SquareSum(n-1)
    return s
print("\n\t sum of squares : ",SquareSum(4)) 
#  sum of squares :  30

""" 1+4+9+16 = 30"""




print("\n\t first n natural numbers ",end=" ")
def N(n):
    if n>0:
        N(n-1)
        print(n,end="")
        
    return "\n\t return :  none" 
print(N(5))


	#  first n natural numbers  12345
	#  return :  none



    