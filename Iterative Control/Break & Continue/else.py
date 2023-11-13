"""
else with while loop 
while condition:
        code
        code
else:
        code 

"""
"""
    else block executes when while loop terminates normally 
    else block won't be execute when loop terminates due to break statement.

"""

i=1
while i<=3:
    a=int(input("\n\t Enter a num : "))
    if a%2 == 0 :
        print("\n\t Tum insan ho ")
        break
    i+=1
else:
    print("\n\t Tum gade ho ")
print("\n")


        #  Enter a num : 2

        #  Tum insan ho 