#name:
#date:

from Athlete import *

class Pirate(Athlete):
    def __init__(self, world):
        Athlete.__init__(self, world, 1, 1, east, 0)
        
    def approachPile(self):
        while not self.nextToABeeper():
            self.move()
        
 
    def numOfBeepersInPile(self):
        counter=0
        while self.nextToABeeper():
            self.pickBeeper()
            counter+=1
        return counter
 
    def turnAppropriately(self, beepers):
        if beepers==1:
            self.turnLeft()
        elif beepers==2:
            self.turnAround()
        elif beepers==3:
            self.turnRight()
        else:
            self.move()


