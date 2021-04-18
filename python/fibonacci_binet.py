'''Fibonacci number at nth position. This program calculate the
   fibonacci number at nth position using Binet's Formula.
   The positional value is taken as user input n. '''


def restart():
    n = input("Please enter the postional value to check Fibonacci number: ")
    if n.isdigit() is True:
        n = int(n)
        c = (((1 + 5**.5) / 2)**n - ((1 - 5**.5) / 2)**n) / 5**.5
        print("The fibonacci number at position " + str(n) + " is " + str(c))
    else:
        print("Please try again...")
        restart()


restart()


while True:
    print("Do you want to check on another position?(y/n) ")
    i = input()
    if i in ("si", "da", "yes", "y"):
        restart()
    else:
        print("Goodbye!")
        break
