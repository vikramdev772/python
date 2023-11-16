""" How to approcah recursive function ? """

#write a recursive funciton to calculate sum of first n natural number

def add(n):
    if(n==0):
        return n
    s=n+add(n-1)
    return s

print("\n\t Sum of n natural num : ",add(100))

    # Sum of n natural num :  5050

print("\n\t sum of n natural numbers : ", end="")

def ns(n):
    if n == 1:
        return 1
    s = n + ns(n - 1)
    for i in range(1, n):
        print(f"{i}+", end="")
    return s

print("\n\t sum : ", ns(5))


    #      Sum of n natural num :  5050

	#  sum of n natural numbers : 1+1+2+1+2+3+1+2+3+4+
	#  sum :  15



    