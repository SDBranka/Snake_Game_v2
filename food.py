import turtle as t
import random

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # standard size is 20x20 so we need to 
        # scale it down
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        self.goto(random.randint(-243, 243), random.randint(-243, 243))
