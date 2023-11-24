
"""write a program which takes user's age and display the category of person .
Age below 10 years - kid , Age below 20 - 
Teen, Age below 40 - young , Age below 60 - experienced , Age above or equal 60 - Senior Citizen ."""


def categorize_person(age):
    match age:
        case x if x < 10:
            return "Kid"
        case x if x < 20:
            return "Teen"
        case x if x < 40:
            return "Young"
        case x if x < 60:
            return "Experienced"
        case _:
            return "Senior Citizen"

# Get user input for age
try:
    age = int(input("\n\tEnter your age: "))
    category = categorize_person(age)
    print(f"\n\tYou are categorized as a {category}.")
except ValueError:
    print("\n\tInvalid input. Please enter a valid age as a number.")


#    Enter your age: 18

#         You are categorized as a Teen.

