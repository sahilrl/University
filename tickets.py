'''This program provides information about the tickets sold
 in the compartments. The element 0 in the tuple means that
 the seat is available whereas the element 1 shows the seat
 is occupied. The output of the program tells if there is even
 one seat left in any compartment and also how many compartments
 are fully occupied.'''
compartment_A = (0, 1, 0, 1)
compartment_B = (0, 1, 1, 1)
compartment_C = (1, 1, 1, 1)
compartment_D = (0, 0, 0, 0)


def checking_seat_A():
    seat_available = 0
    for i in compartment_A:
        if i == 0:
            seat_available += 1
    if seat_available == 0:
        return 1
    else:
        print("Available Seats in compartment A: "+str(seat_available))
        return 0


def checking_seat_B():
    seat_available = 0
    for i in compartment_B:
        if i == 0:
            seat_available += 1
    if seat_available == 0:
        return 1
    else:
        print("Seats in compartment B: "+str(seat_available))
        return 0


def checking_seat_C():
    seat_available = 0
    for i in compartment_C:
        if i == 0:
            seat_available += 1
    if seat_available == 0:
        return 1
    else:
        print("Seats in compartment C: "+str(seat_available))
        return 0


def checking_seat_D():
    seat_available = 0
    for i in compartment_D:
        if i == 0:
            seat_available += 1
    if seat_available == 0:
        return 1
    else:
        print("Seats in compartment D: "+str(seat_available))
        return 0


def full_compartment():
    total_full_compartment = (checking_seat_A() + checking_seat_B() +
                              checking_seat_C() + checking_seat_D())
    print("Total full compartments are: "+str(total_full_compartment))


full_compartment()
