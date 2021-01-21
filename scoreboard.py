from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Arial", 20, "normal")
GAME_OVER_FONT = ("Arial", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=266)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        self.clear()
        self.goto(x=0, y=30)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(x=0, y=0)
        self.write(f"FINAL SCORE: {self.score}", align=ALIGNMENT, font=GAME_OVER_FONT)
