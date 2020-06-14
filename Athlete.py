from pyKarel import *


class Athlete(Robot):
    def turnRight(self):
        self.turnLeft()
        self.turnLeft()
        self.turnLeft()
    def turnAround(self):
        self.turnLeft()
        self.turnLeft()
    def moveAndPut(self):
        self.putBeeper()
        self.move()