from Athlete import *

class Racer(Athlete):
    def __init__(self, world, y):
        Athlete.__init__(self, world, 1, y, east)

    def jumpEast(self):
        while(not self.facingNorth()):
            self.turnLeft()
        self.move()
        self.turnRight()
        self.move()
        self.turnRight()
        self.move()
        self.turnLeft()
    # your code goes here

    def jumpWest(self):
        while (not self.facingNorth()):
            self.turnLeft()
        self.move()
        self.turnLeft()
        self.move()
        self.turnLeft()
        self.move()
        self.turnRight()
    # your code goes here

    def sprint(self, n):
        for x in range(0, n):
            self.move()

    def put(self, n):
        for i in range(0, n):
            self.putBeeper()

    def pick(self, n):
        for i in range(0,n):
            self.pickBeeper()
