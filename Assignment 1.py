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
        self.__x = x
        self.__y = y

    def move(self, x, y):
        self.x += x
        self.y += y
        return (self.x, self.y)


class Pirate(MoveableObject):
    treasure = []
    ''' 
    A class to represent a Pirate in the game.
    '''
    def __init__ (self, x, y, name):
        super().__init__(x, y)
        self.__name = name

    def getTreasure_value(self):
        sum = 0
        for treasure in self.treasure:
            sum += treasure.get_value()
        return sum

    def move(self, a, b):
        position = super().move(a, b)   
        return position
    
    @classmethod
    def add_treasure(self, treasure):
        if isinstance(treasure, Treasure):
            self.treasure.append(treasure)

    


class Ship(MoveableObject):
    treasure = []
    '''
    A class to represent a Ship in the game.
    '''
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self, a, b):
        position = super().move(a, b)   
        return position
    
    def fire_cannon(self):
        pass

    def reload_cannon(self):
        pass

    @classmethod
    def get_treasure_value(self):
        return Pirate.getTreasure_value()
    
    @classmethod
    def add_treasure(self, treasure):
        if isinstance(treasure, Treasure):
            self.treasure.append(treasure)


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
        self.set_name(name)
        self.__value = value

    def set_name(self, name):
        if type(name) == str and len(name) > 0:
            self.__name = name
        else:
            print("Error: Name is invalid.")

    def get_name(self):
        return self.__name
    
    def get_value(self):
        return self.__value
    
    def __str__(self):
        return f"{self.__name} worth {self.__value} gold"



treature = Treasure('Lesly', 400)
treature.get_name()

print(treature)
