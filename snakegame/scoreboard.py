from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')

with open("data.txt") as data:
    result = data.read()

class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(result)
        self.setposition(0, 270)
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score} ", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score

        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)