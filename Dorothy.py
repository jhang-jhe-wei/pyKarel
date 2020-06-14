from Athlete import *


class Dorothy(Athlete):
    def __init__(self, world):
        Athlete.__init__(self, world, 2, 2, east, 0)

    def findPath(self):
        self.turnRight()
        self.move()
        if self.nextToABeeper():
            return True
        self.turnAround()
        self.move()
        self.move()
        if self.nextToABeeper():
            return True
        else:
            self.turnAround()
            self.move()
            return False

    def followPath(self):
        while self.nextToABeeper():
            if not self.frontIsClear():
                return
            self.move()
        self.turnAround()
        self.move()
