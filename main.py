import time
import random
from turtle import Screen
from pad import MyPad, ComputerPad
from score import Score, UserScoreBoard, ComputerScoreBoard, FinalScore
from ball import Ball, SeparationLine


my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(800, 600)
my_screen.listen()
my_screen.tracer(0)

my_line = SeparationLine()
computer_pad = ComputerPad()
my_pad = MyPad()
ball = Ball()
score = Score()



time.sleep(0.1)
my_screen.update()
my_screen.tracer(1)

my_screen.onkeypress(key="Up", fun=my_pad.move_up)
my_screen.onkeypress(key="Down", fun=my_pad.move_down)

my_screen.onkeypress(key="w", fun=computer_pad.move_up)
my_screen.onkeypress(key="x", fun=computer_pad.move_down)

game = True
while game:
    speed = 0.1
    ball.speed("slow")
    computer_score_board = ComputerScoreBoard(score.computer_score)
    my_score_board = UserScoreBoard(score.my_score)

    ball.X = random.choice([10, -10])
    ball.Y = random.choice([10, -10])

    is_game_on = True

    while is_game_on:
        # time.sleep(speed)
        ball.move_ball()
        ball.bounce_back()
        ball.ball_change_dir(my_pad, computer_pad)
        defeat = score.check_for_score(ball, my_pad, computer_pad)
        if speed > 0:
            speed *= 0.9

        if defeat:
            computer_score_board.clear()
            my_score_board.clear()
            computer_score_board.clear()
            my_score_board.clear()
            ball.teleport(0,0)
            my_pad.teleport(350, 0)

            computer_pad.teleport(-350, 0)
            is_game_on = False

        if score.computer_score == 7 or score.my_score == 7:

            if score.computer_score == 7:
                final_score = FinalScore("Player1 wins")
            else:
                final_score = FinalScore("Player2 wins")
            game = False

computer_score_board = ComputerScoreBoard(score.computer_score)
my_score_board = UserScoreBoard(score.my_score)

























my_screen.exitonclick()

