from Athlete import Athlete
from pyKarel import *

record = {}


def karelPick(arg):
    for i in range(8):
        print i
        record[i] = 0
        while arg.nextToABeeper():
            arg.pickBeeper()
            record[i] += 1
        arg.move()


def karelPut(arg):
    for i in range(7, -1, -1):
        print i
        for j in range(record[i]):
            arg.putBeeper()
        arg.move()


def main():
    name_of_world = raw_input("Which 'pile'? ")
    wld = World(name_of_world, width=8, height=3, delay=0.1)
    karel = Athlete(wld, 1, 1, east, 0)
    karelPick(karel)
    karel.turnAround()
    karelPut(karel)
    wld.mainloop()

if __name__ == "__main__":
    main()
