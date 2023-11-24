""" Write a python program to check whether a given string is multiword string 
or single word string using match case statement"""

def string_type(input_string):
    match input_string.split():
        case[_]:
            return "\n\t Single Word String "
        case _:
            return "\n\t Multiword String \n"


user_input = input("\n\t Enter a string : ")
result = string_type(user_input)

print(f"\n\t The given string is a {result} .")

#   Enter a string : Vikram ram

#          The given string is a
#          Multiword String
#  .

#  Enter a string : Vikram_ram

#          The given string is a
#          Single Word String  .


