'''This program provides information about the tickets sold
 in the compartments. The element 0 in the tuple means that
 the seat is available whereas the element 1 shows the seat
 is occupied. The output of the program tells if there is even
 one seat left in any compartment and also how many compartments
 are fully occupied.'''
import random


def compartment():
    compartments = []
    while True:
        try:
            number_of_compartments = int(input("Enter the number"
                                               "of Compartments: "))
            break
        except ValueError:
            print("Wrong input! Please enter an integer value.")
    for i in range(number_of_compartments):
        my_randoms = tuple(random.randrange(0, 2) for _ in range(4))
        compartments.append(my_randoms)
    return compartments


def checking_seat():
    compartments = compartment()
    list_empty = []
    var = 0
    for i in range(0, len(compartments)):
        comp = compartments[i]
        total_seats_available = 0
        for j in range(0, len(comp)):
            if comp[j] == 0:
                total_seats_available += 1
        list_empty.append(total_seats_available)
        if list_empty[i] == 0:
            var += 1
    print(compartments)
    print("Total full compartments: "+str(var))
    for z in range(len(compartments)):
        names_compartment = [i for i in range(1, len(compartments)+1)]
        if list_empty[z] != 0:
            print("Seats available in Compartment "
                  "%s: %s" % (names_compartment[z], list_empty[z]))


checking_seat()
