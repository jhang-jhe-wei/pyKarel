from Athlete import *
def takeTheField(arg):
    arg.turnLeft()
    arg.move()
    arg.move()
    arg.move()
    arg.move()
    arg.turnRight()
    arg.move()
    arg.move()
wld=World("arena")
coach=Athlete(wld,2,7,east,0)
athlete1=Athlete(wld)
athlete2=Athlete(wld)
athlete3=Athlete(wld)
athlete4=Athlete(wld)
athlete5=Athlete(wld)
athlete6=Athlete(wld)
takeTheField(athlete1)
athlete1.move()
athlete1.move()
athlete1.move()
athlete1.turnLeft()
athlete1.move()
athlete1.move()
athlete1.turnAround()
takeTheField(athlete2)
athlete2.move()
athlete2.move()
athlete2.move()
athlete2.move()
athlete2.move()
athlete2.turnLeft()
athlete2.move()
athlete2.turnAround()
takeTheField(athlete3)
athlete3.move()
athlete3.move()
athlete3.move()
athlete3.move()
athlete3.turnRight()
takeTheField(athlete4)
athlete4.move()
athlete4.move()
athlete4.move()
athlete4.turnRight()
takeTheField(athlete5)
athlete5.move()
athlete5.move()
athlete5.turnRight()
takeTheField(athlete6)
athlete6.move()
athlete6.turnLeft()
athlete6.move()
athlete6.turnAround()
wld.mainloop()