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
