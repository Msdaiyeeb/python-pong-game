from turtle import Turtle
import random



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(1)
        self.color("white")
        self.shape("square")
        self.shapesize(1, 1)
        self.X = random.choice([10, -10])
        self.Y = random.choice([10, -10])

    def move_ball(self):
        self.goto(self.xcor() + self.X, self.ycor() + self.Y)

    def bounce_back(self):
        if self.ycor() == 290 or self.ycor() == -290:
            if self.ycor() == 290:
                self.Y = -10
            else:
                self.Y = 10

    def ball_change_dir(self, my_pad ,my_pad2):
        if self.distance(my_pad) < 20:
            self.X = -10
        elif self.xcor() == 340 and self.distance(my_pad) < 50:
            self.X = -10
        elif self.distance(my_pad2) < 20:
            self.X = 10
        elif self.xcor() == -340 and self.distance(my_pad2) < 50:
            self.X = 10


class SeparationLine(Turtle):
    def __init__(self):
        super().__init__()
        self.isvisible()
        self.shape("square")
        self.penup()
        self.teleport(0, 300)
        self.setheading(270)
        self.pencolor("white")
        self.pensize(5)
        self.move_line()

    def move_line(self):
        for _ in range(0, 40):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)
