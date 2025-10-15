from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.left_score=0
        self.right_score=0
        self.update_score()
    def l_piont(self):
        self.left_score+=1
        self.update_score()
    def r_piont(self):
        self.right_score+=1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,250)
        self.write( self.left_score, align="center", font=("courier", 24, "bold"))
        self.goto(100,250)
        self.write(self.right_score, align="center", font=("courier", 24, "bold"))