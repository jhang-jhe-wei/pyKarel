from Racer import *
def task(arg):
    arg.move()
    arg.jumpEast()
    arg.sprint(2)
    arg.pick(7)
    arg.sprint(2)
    arg.pick(5)
    arg.sprint(2)
    arg.pick(3)
    arg.turnAround()
    arg.sprint(6)
    arg.jumpWest()
    arg.move()
    arg.put(arg.beepers)
    arg.turnAround()
    arg.move()
wld=World("shuttle",50,True,0.1,True,10,10)
racer1=Racer(wld,1)
racer2=Racer(wld,4)
racer3=Racer(wld,7)
task(racer1)
task(racer2)
task(racer3)
wld.mainloop()