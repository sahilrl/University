import math


def errorhandle():
    print("Wrong Input! Try again?(y/n)")
    user = input()
    if user in ["y", "yes", "si", "da"]:
        main()
    else:
        print("goodbye!")


def polynomial():
    global K, N
    K = 4
    N = 4
    arr = []
    i = [*range(1, K+1)]
    j = [*range(1, N+1)]
    for n in i:
        for k in j:
            x = (((k+math.sqrt(k**2-1))**(n+1) -
                 (k-math.sqrt(k**2-1))**(n+1)))
            y = (2 * math.sqrt(k**2-1))
            try:
                poly = round(x/y)
            except ZeroDivisionError:
                poly = 0
            arr.append(poly)
    return arr


def createMatrix(rowCount, colCount, dataList):
    global mat
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            rowList.append(dataList[rowCount * i + j])
        mat.append(rowList)
    print(mat)


def main():
    arr = polynomial()
    createMatrix(K, N, arr)
    # print(K)
    # print(mat)
    increment()


def increment():
    print("1. Enter 1 for adding a row.")
    print("2. Enter 2 for adding a column.")
    print("3. Enter 3 for adding both simultaneously")
    usr = (input())
    if usr == "1":
        add = [sum(i) for i in mat]
        for z in range(K):
            mat[z].extend([add[z]])
        print(mat)
    elif usr == "2":
        add = [sum(i) for i in zip(*mat)]
        mat.append(add)
        print(mat)
    elif usr == "3":
        row = [sum(i) for i in mat]
        for z in range(K):
            mat[z].extend([row[z]])
        column = [sum(i) for i in zip(*mat)]
        mat.append(column)
        print(mat)
    else:
        errorhandle()


main()
