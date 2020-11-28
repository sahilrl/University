'''This program provides information about the tickets sold
 in the compartments. The element 0 in the tuple means that
 the seat is available whereas the element 1 shows the seat
 is occupied. The output of the program tells if there is even
 one seat left in any compartment and also how many compartments
 are fully occupied.'''
compartments = [(1, 0, 1, 0), (0, 0, 0, 0), (1, 1, 1, 1), (0, 1, 1, 1)]


def checking_seat():
    a = b = c = d = total_filled_seats = total_seats_available = 0
    for i in range(0, len(compartments)):
        comp = compartments[i]
        # print(comp)
        for j in range(0, len(comp)):
            seat = comp[j]
            if seat == 0:
                total_seats_available += 1
            elif seat == 1:
                total_filled_seats += 1
            if i == 0:
                if seat == 0:
                    a += 1
                if a == 0:
                    p = 1
                else:
                    p = 0
            elif i == 1:
                if seat == 0:
                    b += 1
                if b == 0:
                    q = 1
                else:
                    q = 0
            elif i == 2:
                if seat == 0:
                    c += 1
                if c == 0:
                    r = 1
                else:
                    r = 0
            elif i == 3:
                if seat == 0:
                    d += 1
                if d == 0:
                    s = 1
                else:
                    s = 0
    total_full_compartments = p + q + r + s
    print("Total full Compartments: "+str(total_full_compartments))
    print("Total occupied seats: "+str(total_filled_seats))
    print("Total seats available: "+str(total_seats_available))
    print("Total seats in Compartment A: "+str(a))
    print("Total seats in Compartment B: "+str(b))
    print("Total seats in Compartment C: "+str(c))
    print("Total seats in Compartment D: "+str(d))


checking_seat()
