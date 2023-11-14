
"""
        for else

        for variable in iterable :
            code
            code
            if condition :
                break
            code 
        else:
            code 
            code 

"""


x=input("\n\t Enter a string : ")

for i in x:
    if i=='r':
        break
    print(i,end=" ")
else:
    print("\n\t All the characters are processed \n")


#          Enter a string : vikram
# v i k

#         Enter a string : python
# p y t h o n
#          All the characters are processed

