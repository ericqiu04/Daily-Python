from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def addScore(self):
        self.score +=1

    def getScore(self):
        return "Score = " + str(self.score)

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font = ('Arial', 24, 'bold    '))