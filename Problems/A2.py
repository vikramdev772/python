# write a menu driven program to perform following opertaions - 
# Addition, Subtraction,Multiplication , Division.


print("\n\t  1, Addition ")
print("\n\t  2, Subtraction ")
print("\n\t  3, Multiplication ")
print("\n\t  4, Division ")
print("\n\t   Enter your choice : ",end=" ")

choice = int(input())

match choice:
    case 1:
        print("\n\t Enter two numbers : ")
        a,b=int(input(),int(input()))
        c=a+b
        print("\n\t Sum : ",c)
    case 2:
        print("\n\t Enter two numbers : ")
        x,y=int(input(),int(input()))
        z=x-y
        print("\n\t Difference : ",z)
    case 3:
        print("\n\t Enter two numbers : ") 
        a,b=int(input(),int(input()))
        print("\n\t Product of : ",(a*b)) 
    case 4:
        print("\n\t Enter two numbers : ")
        p,q=int(input()),int(input())
        print(f"\n\t {p} by {q} : ",str((p/q)))
    case _:
        print("\n\t Invalid Choice \n")

print("\n") 


#  1, Addition

#           2, Subtraction

#           3, Multiplication

#           4, Division

#            Enter your choice :  4

#          Enter two numbers :
# 6
# 2

#          6 by 2 :  3.0




