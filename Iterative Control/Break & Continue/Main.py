"""
        break is a keyword

        break is used to transfer control outside the loop body

        break can only be used in the body of loop 
        break terminates the execution of loop 


"""

i=1
while i<=3:
    a=int(input("\n\t Enter a even num : "))
    if a%2 == 0:
        break
    i+=1
if i==4:
    print("\n\t  not good ")
else:
    print("\n\t it is ok ")
print("\n")


# Enter a even num : 2

#          it is ok 
