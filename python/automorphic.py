"""
On value 34 (neither trimorphic nor automorphic),
On value 24 (Not amorphic but trimorphic),
On value 26 (Neither trimorphic not automorphic),
On value 25 (both automorphic and trimorphic)
"""


def automorphic(num, sq, cube, i):
    while i > 0:
        if num % 10 != sq % 10:
            return False
        else:
            num //= 10
            sq //= 10
            i -= 1
            return True


def trimorphic(num, cube):
    j = len(str(num))
    while j > 0:
        if num % 10 != cube % 10:
            return False

        else:
            num //= 10
            cube //= 10
            j -= 1
    return True


def rerun():
    while True:
        try:
            print("Please enter a number: ")
            num = int(input())

        except ValueError:
            print("Not an integer. try again...")
            continue
        else:
            break

    print('the input number is: '+str(num))
    sq = num*num
    cube = num*num*num
    i = len(str(num))

    if automorphic(num, sq, cube, i):
        print("Automorphic and Trimorphic both")
    else:
        if trimorphic(num, cube):
            print("It's not Automorphic but its Trimorphic")
        else:
            print("It's neither Automorphic nor trimorphic")


rerun()


while True:
    print("Do you want to try another number?(y/n) ")
    repeat = input()
    if repeat in ('y', 'yes', 'si', 'da'):
        rerun()
    else:
        print('Goodbye!')
        break
