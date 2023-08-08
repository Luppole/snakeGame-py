import random
from turtle import Turtle
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # the food position is randomally generated and is now a multiple of 20 so that the player could eat it properly
        random_x = random.randint(-280//20, 280//20)*20
        random_y = random.randint(-280//20, 280//20)*20
        self.goto(random_x, random_y)