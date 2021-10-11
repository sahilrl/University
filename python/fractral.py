'''This program implements Dragon Curve using Lsystem'''

import string
import turtle


COLORS = ['red', 'yellow', 'maroon', 'green', 'blue']

def iterator(axiom, times):
    '''
    This function takes
    axiom and number of times
    iteration as parameter and
    returns a list with contains
    a pattern formed by L-system
    '''
    for _ in range(times):
        axiom = l_sys(axiom)
    return axiom

def l_sys(axiom):
    '''
    This function generate the pattern for Lsys
    param axiom: starting alphabet
    returns: string with the pattern
    '''
    dictionary = {'A': 'A-A++A-A'}
    return ''.join([dictionary.get(c) or c for c in axiom])

def draw(tur, axiom, length, angle):
    ''' Drawing figure
    parameters:
        tur: turtle.Turtle()
        axiom: initial alphabet
        lenght: length of line segment
        angle: angle of rotation
    '''
    for this in axiom:
        if this in string.ascii_letters:
            tur.forward(length)
        elif this == '-':
            tur.left(angle)
        elif this == '+':
            tur.right(angle)

def main() -> bool:
    ''' Main program
    returns: boolean value False'''
    try:
        rang = int(input('Select color for the fractle.\n'
                '1. Red\n2. Yellow\n3. Maroon\n4. Green\n'
                '5. Blue\nPlease enter your option: '))
        length = int(input('Enter lenght of line segment: '))
    except ValueError:
        print('Your input is wrong\nTry Again...')
        main()
    tur = turtle.Turtle()
    tur.speed(1000)
    win = turtle.Screen()
    win.bgcolor('black')
    tur.color(COLORS[rang])
    tur.pensize(5)
    tur.penup()
    tur.setposition(-150, 0)
    tur.pendown()
    tur.speed(0)
    axiom = 'A'
    angle = 60
    times = 4
    draw(tur, iterator(axiom, times), length, angle)
    win.exitonclick()
    return False

if __name__ == '__main__':
    while main():
        pass
