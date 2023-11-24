

l=[1,2,3,1,3,2,5,67,5,4,3,2,10]
print(set(l))
# {1, 2, 67, 3, 5, 4, 10}

print(list(set(l)))
# [1, 2, 67, 3, 5, 4, 10]

"""Acessing the set elements"""

s=[1,23,4,5,66,7,9,6,5]
s=list(set(s))
for e in s:
    print(e)



#     [1, 2, 67, 3, 5, 4, 10]
# 1
# 23
# 4
# 5
# 66
# 7
# 9


# [1, 2, 67, 3, 5, 4, 10]
# 1
# 66
# 4
# 5
# 6
# 7
# 9
# 23


""" Built in methods 
    len()
    min()
    max()
    sum()
    sorted()

"""

print(len(s))  #8

print(sum(s))  #121

"""comparison operator 
    Two set objects are equal  if their elements are same , doesn't matter 
    the order of elements.
"""


s1={8,1,5}
print(s1)
s2={5,1,8}
print(s2)

# {8, 1, 5}
# {8, 1, 5}

print(s1>s2) #False
print(s1<s2) #False