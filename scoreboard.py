from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.number = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.number}", False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.number}", False, align=ALIGNMENT, font=FONT)

    def add(self):
        self.number += 1
        self.clear()
        self.update_scoreboard()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
