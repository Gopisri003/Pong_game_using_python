from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_points = 0
        self.r_points = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_points, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=self.r_points, align="center", font=("Courier", 80, "normal"))

    def l_score(self):
        self.l_points += 1
        self.update_score()

    def r_score(self):
        self.r_points += 1
        self.update_score()

