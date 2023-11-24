"""set comprehension
s1={expression for e in object }

s=input("Enter a String ")
s1={e for e in s if e in "aeiou"}
"""

s=input("\n\t Enter a string : ")
s1={e for e in s if e in "aeiou"}
print("\n\t vowels are in the string : ",s1)


#  Enter a string : vikram

#          vowels are in the string :  {'i', 'a'}


"""
    for e in s:
        if e in "aeiou":
            s1.add(e)
"""

# x = input("\n\t Enter elements separated by comma : ")
# y = {e for e in x.split(',')}
# print(y)
# z = {eval(e) for e in x.split(',')}
# print("\n\t ", z)

x = input("\n\t Enter elements separated by comma : ")

try:
    y = {e for e in x.split(',')}
    print(y)

    z = {int(e) for e in x.split(',')}
    print("\n\t ", z)

except ValueError as ve:
    print(f"Error: {ve}")

#  Enter elements separated by comma : vikram,mark,42,stark,tony
# {'tony', 'stark', '42', 'mark', 'vikram'}

print("\n\t Set comprehension with conditional expression\n")


n = {x if x % 2 == 0 else -x for x in range(1, 6)}
print(n)





