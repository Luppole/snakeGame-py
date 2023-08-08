from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

borders_x=[screen.window_width()//2, -1*(screen.window_width()//2)]
borders_y=[screen.window_height()//2, -1*(screen.window_height()//2)]

game_is_on = True
while game_is_on:
    screen.update()
    
    current_position=(snake.head.pos()[0], snake.head.pos()[1])
    food_position=(food.pos()[0], food.pos()[1])
    # Checks if the player is out of bounds
    if current_position[0] in borders_x or current_position[1] in borders_y:
        scoreboard.game_over()
        time.sleep(0.5)
    # Cheks if the player ate the food
    elif current_position == food_position:
        snake.extend()
        food.refresh()
        

    
    time.sleep(0.1)

    snake.move()


screen.exitonclick()