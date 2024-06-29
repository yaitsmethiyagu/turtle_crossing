from turtle import *
import time


class Score:
    def __init__(self):
        self.message = None
        self.level = 1

    def player_won(self, message):
        self.message = Turtle()
        self.message.penup()
        self.message.color("black")

        if message == "won":
            self.level += 1
            self.message.write(f"YOU WON\nLevel - {self.level}", move=True, align="center",
                               font=("Terminal", 35, "bold"))
        else:
            self.message.write(message, move=False, align="center", font=("Terminal", 35, "bold"))
        self.message.hideturtle()
        Screen().update()
        time.sleep(3)
        self.message.clear()
        Screen().update()
