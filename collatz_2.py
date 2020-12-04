'''Эта программа реализует проверку гипотезы Коллатца для
 чисел между заданным диапазоном.
 This program implements hypothesis testing of collatz for
 numbers between a specified range.'''


def taking_input():
    '''This function takes the user input A and B'''
    print("This program will do the hypothesis testing of"
          "of numbers from range A to B")
    try:
        n = int(input("Enter number A ---> [A,B): "))
    except ValueError:
        n = 0
    try:
        c = int(input("Enter number A ---> [%s,B): " % n))
    except ValueError:
        c = None
    generator(n, c)


def generator(n=0, b=None):
    '''This function takes the range and generate collatz numbers'''
    if b is not None:
        c = range(n, b)
        print(c)
        for n in c:
            steps = 0
            print("The initializer is: "+str(n))
            while n != 1:
                if n % 2 == 0:
                    n = n / 2
                elif n % 2 == 1:
                    n = (3*n) + 1
                steps += 1
                print(int(n))
            print("Total Steps: " + str(steps) + "\n\n")
    else:
        while True:
            count = n
            steps = 0
            print("The initializer is: "+str(n))
            while n != 1:
                if n % 2 == 0:
                    n = n / 2
                elif n % 2 == 1:
                    n = (3*n) + 1
                steps += 1
                print(int(n))
            print("Total Steps: " + str(steps) + "\n\n")
            count += 1
            n = count


taking_input()
