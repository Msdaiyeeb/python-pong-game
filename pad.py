import time
from turtle import Turtle


class MyPad(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.teleport(350, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def color_for_lose(self,lose):
        if lose:
            self.color("red")
            time.sleep(0.2)
            self.color("white")
            time.sleep(0.2)
            self.color("red")
            time.sleep(0.2)
            self.color("white")


class ComputerPad(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.teleport(-350, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)


    def color_for_computer_lose(self,lose):
        if lose:
            self.color("red")
            time.sleep(0.2)
            self.color("white")
            time.sleep(0.2)
            self.color("red")
            time.sleep(0.2)
            self.color("white")

