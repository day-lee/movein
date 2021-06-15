from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ('Courier', 30, 'bold')


class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()


    def update_text(self):
        self.penup()
        self.color("white")
        self.write(arg="Good Job!", move=False, font=FONT)

    def text_refresh(self):
        self.goto(100, 100)
        self.update_text()



