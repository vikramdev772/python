# def Aveg(a,b,c):
#     A=(a+b+c)/2
#     return A

# print("\n\t Average : ",Aveg(10,20))
# print("\n\t Average : ",Aveg(10,20,4,5,6,7,8))
# print("\n\t Average : ",Aveg(10,20,2,1,5,6))
# print("\n\t Average : ",Aveg(10,20,24,21,12,6,14,8,9,10))


print("\n\t Variable lenght arguments \n")


def Aveg(*t):
    A=sum(t)/len(t)
    return A

print("\n\t Average : ",Aveg(10,20))
print("\n\t Average : ",Aveg(10,20,4,5,6,7,8))
print("\n\t Average : ",Aveg(10,20,2,1,5,6))
print("\n\t Average : ",Aveg(10,20,24,21,12,6,14,8,9,10))


# Variable lenght arguments


#          Average :  15.0

#          Average :  8.571428571428571

#          Average :  7.333333333333333

#          Average :  13.4


# """
#     Variable length arguments 

#     def f1(*t):
#             t = tuple
#     f1(10)
#     f1(10,20)
#     f1(10,20,30,40)
#     passing tuple ..
# """


# You cannot have positonal arguments after keyword arguments f1(b=3,2)


