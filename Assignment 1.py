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
        '''The initilizer method for MoveAbleObject.
        Constructs a MoveableObject with the positional arguments x and y.'''
        self.__x = x
        self.__y = y
        self.__treasure = []

    def move(self, x, y):
        '''The method that moves the object to position(x, y)'''
        self.__x += x
        self.__y += y
        return (self.__x, self.__y)
    
    def get_position(self):
        '''The method that returns the position of the object'''
        return (self.__x, self.__y)
    
    def set_x_position(self, x):
        '''The method that sets the x position of the object'''
        self.__x = x
        return (self.__x)
    
    def set_y_position(self, y):
        '''The method that sets the x position of the object'''
        self.__y = y
        return (self.__y)
    
    def add_treasure(self, treasure):
        '''A class method that adds treasure to the object'''
        if isinstance(treasure, Treasure):
            self.__treasure.append(treasure)
            return self.__treasure

    def get_treasure_list(self):
        '''A method that returns the treasure list of the object'''
        return self.__treasure
    
    def getTreasure_value(self):
        '''A method that gets the sum toatl value of treasures in the objects treasure list.'''
        sum = 0
        for treasure in self.__treasure:
            if self.__treasure != []:
                sum += treasure.get_value()
        return sum

    def __str__(self):
        '''A method that returns a string representation of the object'''
        return f"A moveable object at position {self.get_position()} with treasure {self.get_treasure_list()}"

class Pirate(MoveableObject):
    ''' 
    A class to represent a Pirate in the game.
    '''
    def __init__ (self, x, y, name):
        '''The initializer method of the class Pirate, it uses super to set the x and y position, and sets the name'''
        super().__init__(x, y)
        self.__name = name
        self.__ship = None


    def get_name(self):
        '''The method that returns the name of the pirate'''
        return self.__name
    
    def set_name(self, name):
        '''The method that sets the name of the pirate'''
        self.__name = name
        return self.__name

    def getTreasure_value(self):
        '''The method that implements the superclass method, getTreasure_value, to return the value of the treasure'''
        return super().getTreasure_value()
    
    def set_ship(self, s):
        '''The method that sets the ship of the pirate'''
        if s.get_position() == self.get_position():
            self.__ship = s
        else:
            print("Error: They are not in the same position.")
        # a = self.__x
        # b = self.__y
        # self.__ship = Ship(a, b) #composition

    def get_ship(self):
        '''the method that returns the ship of the pirate'''
        return f"Ship at position {self.get_position()}"


    def move(self, a, b):
        '''The method that moves the pirate and the ship the pirate is controlling'''
        position = super().move(a, b)
        if self.__ship != None:
            self.__ship.move(a,b)
        return (position)
    
    def add_treasure(self, treasure):
        '''A method that checks if what is being added to the treasure list is a treasure, then adds it to the pirates list of treasures if there is a treasure'''
        if isinstance(treasure, Treasure):
            if len(self.get_treasure_list()) >= 0 and len(self.get_treasure_list()) <= 5:
                super().add_treasure(treasure)
                return treasure
            
    

        

    


class Ship(MoveableObject):
    '''
    A class to represent a Ship in the game.
    '''
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self, a, b):
        '''The method that moves the ship'''
        position = super().move(a, b)   
        return position
    
    def create_cannon(self):
        '''The method that creates the cannon'''
        self.cannon = Cannon()
        return self.cannon
    
    def _fire(self):
        '''The method that fires the cannon'''
        if len(self.cannonBalls) == 1:
            self.cannonBalls.pop()
            return float(len(self.cannonBalls))

    @classmethod
    def reloading_cannon(self):
        '''A class method that reloads the cannon'''
        if len(self.cannonBalls) == 0:
            self.cannonBalls.append(CannonBall())

    def getTreasure_value(self):
        '''A method that returns the value of the treasure in the ship'''
        return super().getTreasure_value()
    
    def add_treasure(self, treasure):
        '''A method that adds a treasure to the ships treasure list, it first checks if what is being added is a treasure'''
        if isinstance(treasure, Treasure):
            if len(self.treasure) >= 0 and len(self.treasure) <= 20:
                super().add_treasure(treasure)
        
    def treasure_listGet(self):
        '''A method that returns the list of treasures in the ship'''
        return super().get_treasure_list()
    
    

    
    


class Cannon:
    '''
    A class to represent a Cannon in the game.
    '''
    
    def __init__(self):
        '''The initializer method of the class Cannon'''
        self.__cannonBalls = []

    def get_cannoballs(self):
        '''The method that returns the cannon balls list'''
        return self.__cannonBalls
    
    def set_cannonball(self, cb):
        '''cb is a ccannonball'''
        if isinstance(cb, CannonBall):
            self.__cannonBalls.appen(cb)
            return self.__cannonBalls
        else:
            print("Error: You cannot add what is not a cannon ball.")
    

    def _fire(self):
        '''The metod that fires the cannon, and subtracts the fired cannonball from the cannonball list '''
        if len(self.__cannonBalls) == 1:
            for cannonBall in self.__cannonBalls:
                return (float(cannonBall.get_damage()))


            


class CannonBall:
    '''
    A class to represent a CannonBall in the game.
    '''

    def __init__(self, damage):
        '''The initializer method of the class CannonBall, it sets the attribute, damage, and sets the cannonBall to zero.
        '''
        self.__damage = damage
        self.cannonball = 0

    def create_cannonball(self):
        '''A method that creates a cannonBall '''
        self.cannonball += 1
        return self.cannonball
    
    def get_damage(self):
        '''A method that returns the amount of damage for a cannonBall'''
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
        '''A method that sets the name of the treasure'''
        if type(name) == str and len(name) > 0:
            self.__name = name
        else:
            print("Error: Name is invalid.")

    def get_name(self):
        '''A method that returns the name of the treasure'''
        return self.__name
    
    def set_value(self, value):
        '''A method that sets the value of the treasure'''
        self.__value = value
    
    def get_value(self):
        '''A method that returns the value of the treasure'''
        return self.__value
    
    def __str__(self):
        '''A method that returns a string presentation of the treasure object'''
        return f"{self.__name} worth {self.__value} gold"
    
    def __repr__(self):
        '''A mehtod that returns a string reperesentation of the treasure object'''
        return f"{self.__name} worth {self.__value} gold"




'''Testing classes'''

'''MoveableObject'''
m = MoveableObject(12, 5)
print(m.get_position())
m.move(4, 8)
print(m.get_position())
m.set_x_position(4)
print(m.get_position())
m.set_y_position(8)
print(m.get_position())
print(m.get_treasure_list())
print(m.getTreasure_value())
print(m)
t = Treasure('Mercury', 300)
m.add_treasure(t)
print(m)



'''Pirate'''
p = Pirate(6, 4, "Adanna Ugwu")
print(p.get_name())
print(p.get_position())
p.add_treasure(Treasure('Duck', 0.25))
p.add_treasure(Treasure('Hammer', 2))
print(p.get_treasure_list())
print(p.getTreasure_value())
p.set_x_position(10)
print(p.get_position())
a = p.set_ship(Ship(10, 10))
print(p.get_ship())
p.move(5, 2)
print(p.get_position())
b = p.set_ship(Ship(15, 6))
p.move(5, 2)
print(p.get_ship())
p.set_y_position(4)
print(p.get_position())




















'''treature = Treasure('Lesly', 400)
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
print(p.get_ship().get_position())'''

