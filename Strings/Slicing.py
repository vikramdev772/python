print("\n\t Slicing operator ")

"""
        built in mehtods 

        len()
        min()
        max()
        sum()
        sorted()

"""

s="VikrAm"
print("\n\t Length of string :",len(s))  #   Length of string : 6
print("\n\t Min : ",min(s))
print("\n\t Max : ",max(s))

# Min :  A

# Max :  r


str="345612"
print(sorted(str))
# ['1', '2', '3', '4', '5', '6']


print(sum([int(e) for e in str]))

# 21

s1="1a2b3c"
print(int(e) for e in s1 if eval(e)==int)

# <generator object <genexpr> at 0x000001B288C3F780>

print(sum([int(e) for e in s1 if ord(e)>=49 and ord(e)<=57])) #6


x=sorted(s1)

print(x)

