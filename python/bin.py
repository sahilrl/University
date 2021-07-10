import sys


# def taking_input():
#     list = []
#     comp = '10'
#     string_input = input("Please enter a string of "
#                          "0's and 1's without any space: ")
#     for i in string_input:
#         if i not in comp:
#             print("Not a binary...exiting.")
#             sys.exit()
#         else:
#             list.append(i)
#     return list


def checking(taking_input):
    cont = []
    tnoc = []
    cont.append(taking_input[1:5])
    for i in cont[0]:
        if i == "0":
            tnoc.append(1)
        elif i == "1":
            tnoc.append(0)
    taking_input[1:5] = tnoc
    listToStr = ' '.join(map(str, taking_input))
    count = 0
    for i in listToStr:
        if i == "1":
            count += 1
    return listToStr, count


list = taking_input()
listToStr, count = checking(list)
print("Output: "+str(listToStr))
print("Units: "+str(count))
