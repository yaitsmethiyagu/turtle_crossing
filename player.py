from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setpos(0,-280)






    def up(self):
        if self.ycor() < 310:
            self.forward(20)

    def down(self):
        if self.ycor() > -280:
            self.backward(20)

    def player_reset(self):
        self.setpos(0, -280)

    def check_path(self, location):
        self.pendown()
        new_turle = self.clone()
        new_turle.setpos(self.position())
        self.goto(location)