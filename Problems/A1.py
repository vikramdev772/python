
month = int(input("\n\t Enter month number : "))
match month:
    case month if month in (1,3,5,7,8,10,12):
        print("\n\t 31 Days \n")
    case month if month in (4,6,9,11):
        print("\n\t 30 Days \n")
    case 2:
        print("\n\t 28 or 29 Days \n")
    case _:
        print("\n\t Invalid Month number \n")
print()
#   Enter month number : 7

#          31 Days 



