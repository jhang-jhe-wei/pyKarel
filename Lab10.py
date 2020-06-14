from Athlete import Athlete
from pyKarel import *

def main():
    name_of_world = raw_input("Which 'maze'? ")
    wld = World(name_of_world, width=10, height=10, delay=0.1)
    karel=Athlete(wld)
    while not karel.nextToABeeper():
        if karel.rightIsClear():
            karel.turnRight()
            karel.move()
        elif karel.frontIsClear():
            karel.move()
        else:
            karel.turnLeft()
    wld.mainloop()
if __name__=="__main__":
    main()