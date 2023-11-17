
"""
            Foramt

            String .format(var1,var2,...)

            print("{ } how are you ?".format("vikram"))

            print("{} ,{} ,{} ".format("one",25,3.5))

            print("{2},{0},{1}".format(10,20,30))

            
"""

s1="vikram"
print(s1.isupper())
print(s1.islower())
# False
# True

s2="{},welcome"

print(s2.format("Vikram"))
# Vikram,welcome


a=5
b=4.5

s3="value a : {} and b is {}"
print(s3.format(a,b))

# value a : 5 and b is 4.5


