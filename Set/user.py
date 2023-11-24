
s=input("\n\t Enter elements separated by coma :  ")
s1={eval(e) for e in s.split(',')}
print(s1)
#    Enter elements separated by coma :  1,6,7,8,9
# {1, 6, 7, 8, 9}
i={int(e) for e in s.split(',')}
print(i)

#          Enter elements separated by coma :  8,9,0,7,6,6
# {0, 6, 7, 8, 9}
# {0, 6, 7, 8, 9}




