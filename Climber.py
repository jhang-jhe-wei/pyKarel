from Athlete import *
class Climber(Athlete):
    def __init__(self, world, x, y=1, direction=north, beepers=1):
        Athlete.__init__(self, world, x, y, direction, beepers)

    def climbUpRight(self):
        while(self.facingNorth()==False):
            self.turnLeft()
        self.move()
        self.move()
        self.turnRight()
        self.move()
    def climbDownRight(self):
        while (self.facingEast()==False):
            self.turnLeft()
        self.move()
        self.turnRight()
        self.move()
        self.move()
        self.turnLeft()
    def climbUpLeft(self):
        while (self.facingNorth()==False):
            self.turnLeft()
        self.move()
        self.move()
        self.turnLeft()
        self.move()
    def climbDownLeft(self):
        while (self.facingWest()==False):
            self.turnLeft()
        self.move()
        self.turnLeft()
        self.move()
        self.move()
        self.turnRight()