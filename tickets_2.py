'''This program provides information about the tickets sold
 in the compartments. The element 0 in the tuple means that
 the seat is available whereas the element 1 shows the seat
 is occupied. The output of the program tells if there is even
 one seat left in any compartment and also how many compartments
 are fully occupied.'''
compartments = [(1, 0, 1, 0), (0, 0, 0, 0), (1, 1, 1, 1), (0, 1, 1, 1)]


def checking_seat():
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
    print("Total full compartments: "+str(var))
    for z in range(4):
        names_compartment = ["A", "B", "C", "D"]
        if list_empty[z] != 0:
            print("Seats available in Compartment"
                  "%s: %s" % (names_compartment[z], list_empty[z]))


checking_seat()
