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
        self.__treasure = []

    def move(self, x, y):
        self.__x += x
        self.__y += y
        return (self.__x, self.__y)
    
    def get_position(self):
        return (self.__x, self.__y)
    
    @classmethod
    def add_treasure(self, treasure):
        if isinstance(treasure, Treasure):
            self.__treasure.append(treasure)

    def get_treasure_list(self):
        return self.__treasure
    
    def getTreasure_value(self):
        sum = 0
        for treasure in self.__treasure:
            sum += treasure.get_value()
        return sum


class Pirate(MoveableObject):
    ''' 
    A class to represent a Pirate in the game.
    '''
    def __init__ (self, x, y, name):
        super().__init__(x, y)
        self.__name = name
        self.__ship = None


    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        return self.__name

    def getTreasure_value(self):
        return super().getTreasure_value()
    
    def set_ship(self, s):
        if s.get_position() == self.get_position():
            self.__ship = s
        else:
            print("Error: They are not in the same position.")
        # a = self.__x
        # b = self.__y
        # self.__ship = Ship(a, b) #composition

    def get_ship(self):
        return self.__ship


    def move(self, a, b):
        position = super().move(a, b)
        return (position)
    
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
    
    def _fire(self):
        if len(self.cannonBalls) == 1:
            self.cannonBalls.pop()
            return float(len(self.cannonBalls))

    @classmethod
    def reloading_cannon(self):
        if len(self.cannonBalls) == 0:
            self.cannonBalls.append(CannonBall())

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
    
    def __init__(self):
        self.__cannonBalls = []

    def get_cannoballs(self):
        return self.__cannonBalls
    
    def set_cannonball(self, cb):
        '''cb is a ccannonball'''
        pass

    def _fire(self):
        if len(self.__cannonBalls) == 1:
            for cannonBall in self.__cannonBalls:
                return (float(cannonBall.get_damage()))


            


class CannonBall:
    '''
    A class to represent a CannonBall in the game.
    '''

    def __init__(self, damage):
        '''
        '''
        self.__damage = damage
        self.cannonball = 0

    def create_cannonball(self):
        ''' '''
        self.cannonball += 1
        return self.cannonball
    
    def get_damage(self):
        return self.__damage

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


s=Ship(15, 15)
p = Pirate(11, 11, "Potato")
p.set_ship(s)

s=Ship(11, 11)
p = Pirate(11, 11, "Potato")
p.set_ship(s)

pos = p.move(1, 1)
print(pos)
print(p.get_ship().get_position())