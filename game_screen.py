from turtle import Screen, Turtle
import time
class GameScreen():

    def __init__(self):
        self.screen = Screen()
        #self.screen.tracer(0)
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("white")
        self.screen.listen()
        #self.level = 1

    # def player_won(self,message):
    #
    #     self.message = Turtle()
    #     self.message.penup()
    #     self.message.color("black")
    #     if message == "won":
    #         self.level += 1
    #         self.message.write(f"YOU WON\nLevel - {self.level}", move= False, align="center", font= ("Terminal", 35, "bold"))
    #     else:
    #         self.message.write(message, move=False, align="center", font=("Terminal", 35, "bold"))
    #     self.message.hideturtle()
    #     self.screen.update()
    #     time.sleep(3)
    #     self.message.clear()
    #     self.screen.update()

