def cocktail(aList):
    '''This function takes a list and returns a sorted list'''
    nlist = list(aList)
    print("Input list: " + str(nlist))
    size = len(nlist)
    if size < 2:
        return nlist
    swapped = True
    i = 0
    j = size - 1
    while i < j and swapped:
        for k in range(i, j):
            if nlist[k] > nlist[k + 1]:
                nlist[k], nlist[k + 1] = nlist[k + 1], nlist[k]
                swapped = True
        j -= 1
        if swapped:
            swapped = False
            for k in range(j, i, -1):
                if nlist[k] < nlist[k - 1]:
                    nlist[k], nlist[k - 1] = nlist[k - 1], nlist[k]
                    swapped = True
        i += 1
        if not swapped:
            return nlist


aList = input("Enter elements: ")
print("Sorted list: " + str(cocktail(aList)))
