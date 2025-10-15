import random
random_number=random.choice([1,2,3,4,5])


from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.x_move=10
        self.y_move=10

