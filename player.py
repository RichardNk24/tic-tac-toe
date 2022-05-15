import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn.Input(0-9):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
    
    #OtherNonSense
    >> type(1)
    <class 'int'>

    >>> type(15)
    <class 'int'>

    >>> type(0)
    <class 'int'>

    >>> type(-46)
    <class 'int'>
    
    >>> type(4.5)
    <class 'float'>

    >>> type(5.8)
    <class 'float'>

    >>> type(2342423424.3)
    <class 'float'>

    >>> type(4.0)
    <class 'float'>

    >>> type(0.0)
    <class 'float'>

    >>> type(-23.5)
    <class 'float'>
    
    >>> complex(4, 5)
    (4+5j)

    >>> complex(6, 8)
    (6+8j)

    >>> complex(3.4, 3.4)
    (3.4+3.4j)

    >>> complex(0, 0)
    0j

    >>> complex(5)
    (5+0j)

    >>> complex(0, 4)
    4j
    
    # Python Program to find the area of triangle

    a = 5
    b = 6
    c = 7

    # Uncomment below to take inputs from the user
    # a = float(input('Enter first side: '))
    # b = float(input('Enter second side: '))
    # c = float(input('Enter third side: '))

    # calculate the semi-perimeter
    s = (a + b + c) /                                                 2

    # calculate the area
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print('The area of the triangle is %0.2f' %area)
    
    >>> int('2+3')
    Traceback (most recent call last):
      File "<string>", line 301, in runcode
      File "<interactive input>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: '2+3'
    >>> eval('2+3')
    5
    
    >>> x = 12.3456789
    >>> print('The value of x is %3.2f' %x)
    The value of x is 12.35
    >>> print('The value of x is %3.4f' %x)
    The value of x is 12.3457
