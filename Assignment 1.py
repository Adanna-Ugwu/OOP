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
        self.treasure = []

    def move(self, x, y):
        self.x += x
        self.y += y
        return (self.x, self.y)
    
    @classmethod
    def add_treasure(self, treasure):
        if isinstance(treasure, Treasure):
            self.treasure.append(treasure)

    def get_treasure_list(self):
        return self.treasure
    
    def getTreasure_value(self):
        sum = 0
        for treasure in self.treasure:
            sum += treasure.get_value()
        return sum


class Pirate(MoveableObject):
    ''' 
    A class to represent a Pirate in the game.
    '''
    def __init__ (self, x, y, name):
        super().__init__(x, y)
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        return self.__name

    def getTreasure_value(self):
        return super().getTreasure_value()

    def move(self, a, b):
        position = super().move(a, b)   
        return position
    
    def add_treasure(self, treasure):
        if isinstance(treasure, Treasure):
            if len(self.treasure) >= 0 and len(self.treasure) <= 5:
                super().add_treasure(treasure)
                return treasure

    def treasure_listGet(self):
        return super().get_treasure_list()

    


class Ship(MoveableObject):
    '''
    A class to represent a Ship in the game.
    '''
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self, a, b):
        position = super().move(a, b)   
        return position
    
    def create_cannon(self):
        self.cannon = Cannon()
        return self.cannon
    
    def fire_cannon(self):
        pass

    def reload_cannon(self):
        pass

    def getTreasure_value(self):
     return super().getTreasure_value()
    
    def add_treasure(self, treasure):
        if isinstance(treasure, Treasure):
            if len(self.treasure) >= 0 and len(self.treasure) <= 20:
                super().add_treasure(treasure)
        
    def treasure_listGet(self):
        return super().get_treasure_list()


class Cannon:
    '''
    A class to represent a Cannon in the game.
    '''
    cannonBalls = []
    def __init__(self):
        pass

    def _fire(self):
        if len(self.cannonBalls) > 0:
            self.cannonBalls.pop()




class CannonBall:
    '''
    A class to represent a CannonBall in the game.
    '''
    def __init__(self, damage):
        self.__damage = damage
        self.cannonball = 0

    def create_cannonball(self):
        self.cannonball += 1
        return self.cannonball

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
    
    def set_value(self, value):
        self.__value = value
    
    def get_value(self):
        return self.__value
    
    def __str__(self):
        return f"{self.__name} worth {self.__value} gold"
    
    def __repr__(self):
        return f"{self.__name} worth {self.__value} gold"


treature = Treasure('Lesly', 400)
treature.get_name()

print(treature)
