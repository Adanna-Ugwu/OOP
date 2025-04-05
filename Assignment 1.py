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
        list = []
        for treasure in self.__treasure:
            list.append(treasure.__str__())
        return list
        
    def get_treasure(self):
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
            if len(self.get_treasure()) >= 0 and len(self.get_treasure()) <= 5:
                super().add_treasure(treasure)
                return treasure
            
    

        

    


class Ship(MoveableObject):
    '''
    A class to represent a Ship in the game.
    '''
    def __init__(self, x, y):
        super().__init__(x, y)
        self.cannon = None

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
        if self.cannon != None:
            if len(self.cannon.get_cannonBalls()) == 1:
                cannonball = self.cannon.get_cannonBalls().pop()
            
                return (f"Damage of the level {cannonball.get_damage()} done")
            else:
                print("Error: There is no cannonBall to fire. Create a cannonball first.")
        else:
            print("Error: You cannot fire a non-existent cannon.")

    def reloading_cannon(self):
        '''A class method that reloads the cannon'''
        if len(self.cannon.cannonBalls) == 0:
            damage = float(input("Enter the amount of damage for the cannonBall: "))
            s_cannonball = CannonBall(damage)
            self.cannon.cannonBalls.append(s_cannonball)
        else:
            print("Error: There has to be a cannon and the cannonballs to be empty before reloading.")

    def getTreasure_value(self):
        '''A method that returns the value of the treasure in the ship'''
        return super().getTreasure_value()
    
    def add_treasure(self, treasure):
        '''A method that adds a treasure to the ships treasure list, it first checks if what is being added is a treasure'''
        if isinstance(treasure, Treasure):
            if len(self.get_treasure()) >= 0 and len(self.get_treasure()) <= 20:
                super().add_treasure(treasure)

    def __str__(self):
        '''A method that returns a string representation of the ship'''
        return f"A ship at position {self.get_position()} with treasure worth {self.getTreasure_value()} "
    
    

    
    


class Cannon:
    '''
    A class to represent a Cannon in the game.
    '''
    
    def __init__(self):
        '''The initializer method of the class Cannon'''
        self.cannonBalls = []


    def get_cannonballList(self):
        '''The method that returns the cannon balls list'''
        ball_list = []
        for cannonballs in self.cannonBalls:
            ball_list.append(cannonballs.__str__())
        
        return ball_list
    
    def get_cannonBalls(self):
        '''A method that returns the list of cannonballs'''
        return self.cannonBalls
    
    def set_cannonball(self, cb):
        '''cb is a cannonball'''
        if len(self.cannonBalls) == 0:

            if isinstance(cb, CannonBall):
                self.cannonBalls.append(cb)
                return self.cannonBalls
            else:
                print("Error: You cannot add what is not a cannon ball.")
        else:
            print("Error: There is already a cannonball in the cannon. You can only have one at a time, fire the cannon to reload it")
    

    def _fire(self):
        '''The metod that fires the cannon, and subtracts the fired cannonball from the cannonball list '''
        if len(self.cannonBalls) == 1:
            for cannonBall in self.cannonBalls:
                damageDone = f"(Damage of level {float(cannonBall.get_damage())} has been done)"
                self.cannonBalls.pop(0)
                return damageDone
            
        else:
            print("Error: There is no cannonBall in the cannon.")

    def __str__(self):
        '''A  method that returns a string representation of the cannon'''
        return f"A cannon that has a cannonball of damage {[ball.get_damage() for ball in self.cannonBalls]}"


            


class CannonBall:
    '''
    A class to represent a CannonBall in the game.
    '''

    def __init__(self, damage):
        '''The initializer method of the class CannonBall, it sets the attribute, damage, and sets the cannonBall to zero.
        '''
        self.__damage = damage

    def create_cannonball(self):
        '''A method that creates a cannonBall '''
        self.cannonball = 0
        self.cannonball += 1
        return self.cannonball
    
    def get_damage(self):
        '''A method that returns the amount of damage for a cannonBall'''
        return self.__damage
    
    def __str__(self):
        '''A method that returns the string representation of a cannonball'''
        return f"A cannonBall with damage of {self.get_damage()}"

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
t = Treasure('Vintage Vase', 300)
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

'''Ship'''
s = Ship(3, 9)
print(s.get_position())
s.move(7, 11)
print(s.get_position())
c = s.create_cannon()
cb = CannonBall(400)
c.set_cannonball(CannonBall(89))
print(c.get_cannonballList())
c.set_cannonball(cb)
s.add_treasure(Treasure('Couch', 11))
s.add_treasure(Treasure('Screw', 0.3))
print(s.get_treasure_list())
print(s.getTreasure_value())
print(s._fire())
print(s._fire())
s.reloading_cannon()
s.set_x_position(9)
s.set_y_position(14)
print(s.get_position())
c.set_cannonball(CannonBall(48))
print(c.get_cannonballList())


'''Cannon'''
c = Cannon()
print(c.get_cannonballList())
c.get_cannonBalls
c.set_cannonball(CannonBall(48))
print(c.get_cannonballList())
print(c._fire())
c.set_cannonball(CannonBall(32))
print(c.get_cannonballList())
print(c)



'''CannonBall'''
cb = CannonBall(11)
print(cb.get_damage())
print(cb)

'''Treasure'''










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

