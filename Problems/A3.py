"""
write a menu driven program with the following options:

a. Check wheter a given set of three numbers are lengths of an isosceles triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not 
c. Check whether a given set of three numbers are equilatera, triangle or not .
d.Exit."""

def is_isosceles_triangle(a, b, c):
    if a == b or b == c or a == c:
        return True
    else:
        return False

def is_right_angled_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

def is_equilateral_triangle(a, b, c):
    if a == b == c:
        return True
    else:
        return False

while True:
    print("\nMenu:")
    print("a. Check whether a given set of three numbers are lengths of an isosceles triangle or not.")
    print("b. Check whether a given set of three numbers are lengths of sides of a right-angled triangle or not.")
    print("c. Check whether a given set of three numbers are lengths of an equilateral triangle or not.")
    print("d. Exit.")

    choice = input("Enter your choice (a, b, c, or d): ")

    if choice == 'a':
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        result = is_isosceles_triangle(a, b, c)
        print(f"The given set of three numbers {'are' if result else 'are not'} lengths of an isosceles triangle.")

    elif choice == 'b':
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        result = is_right_angled_triangle(a, b, c)
        print(f"The given set of three numbers {'are' if result else 'are not'} lengths of a right-angled triangle.")

    elif choice == 'c':
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        result = is_equilateral_triangle(a, b, c)
        print(f"The given set of three numbers {'are' if result else 'are not'} lengths of an equilateral triangle.")

    elif choice == 'd':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a, b, c, or d.")
