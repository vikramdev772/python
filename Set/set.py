"""set object Methods 
add specified item in a set add iterable(s) elements 
remove item

add()
update()
discard()
remove()
intersection()
union()
clear()
issubset()
issuperset()
pop()



"""


s1={1,2,3,4}
print(s1)
s1.add(5)
print(s1)
s1.add('!')
print("\n\t it is iterable : ",s1)

# {1, 2, 3, 4}
# {1, 2, 3, 4, 5}

#          it is iterable :  {1, 2, 3, 4, 5, '!'}







# s1.add({1,2,3})
# print(s1)    unhashable 

set1={1,2,4,6,7,8}
set1.update([10,20],'ABC',range(20,24,1))
print(set1)



