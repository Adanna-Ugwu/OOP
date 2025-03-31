''' 
This is my own work as defined by the SAIBT Academic Integrity Policy. 
I am fully aware of the consequences of academic misconduct as defined 
by the SAIBT Academic Integrity Policy. 
SAIBT ID:  52243 
Name:   Adanna Ugwu
Date:   25/03/2025
'''

class MoveableObject:
    '''
    A class to represent a moveable object in the game.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pirate:
    ''' 
    A class to represent a Pirate in the game.
    '''
    def __init__ (self, name):
        self.name = name

class Ship:
    '''
    A class to represent a Ship in the game.
    '''

class Cannon:
    '''
    A class to represent a Cannon in the game.
    '''

class CannonBall:
    '''
    A class to represent a CannonBall in the game.
    '''
    def __init__(self, damage):
        self.damage = damage

class Treasure:
    ''' 
    A class to represent the Treasure items that will be stored in a Ship or Pirate. 
    ''' 
    def __init__ (self, name, value):
        '''  
        Constructs a Treasure with the argument name and value.  
        '''
        self.name = name
        self.value = value

 