# create a new scoreboard class that inherits from
# the turtle class. scoreboard will be a turtle that 
# knows how to keep track of the score and how to 
# display it in our program

import turtle as t


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: " + str(self.score),
                    align = "center", 
                    font=("Arial", 24, "normal")
        )


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", 
        align = "center", 
        font=("Arial", 24, "normal")
        )

# turtle.write(arg, move=False, align='left', font='Arial', 8, 'normal')
# Parameters
# arg – object to be written to the TurtleScreen
# move – True/False
# align – one of the strings “left”, “center” or right”
# font – a triple (fontname, fontsize, fonttype)




