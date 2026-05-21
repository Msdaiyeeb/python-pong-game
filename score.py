from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.my_score = 0
        self.computer_score = 0

    def check_for_score(self, ball, my_pad, computer_pad):
        if ball.xcor() > 380 or ball.xcor() < -380:
            if ball.xcor() > 380 :
                my_pad.color_for_lose(True)
                self.computer_score += 1
                return True
            else:
                computer_pad.color_for_computer_lose(True)
                self.my_score += 1
                return True

class ComputerScoreBoard(Turtle):
    def __init__(self,score):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.teleport(-100, 200)
        self.write(score, move= False, align= "center", font=("Fantasy", 24, "normal"))

class UserScoreBoard(Turtle):
    def __init__(self,score):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.teleport(100, 200)
        self.write(score, move= False, align= "center", font=("Fantasy", 24, "normal"))

class FinalScore(Turtle):
    def __init__(self, winner):
        super().__init__()
        self.penup()
        self.color("green")
        self.hideturtle()
        self.write(winner, move=False, align="center", font=("San Serif", 40, "normal"))