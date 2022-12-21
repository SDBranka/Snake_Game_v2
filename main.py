from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# build screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game V2")
# turn off screen animations so that we can use the update() method
screen.tracer(0)

# create scoreboard
scoreboard = Scoreboard()
# create snake
snake = Snake()
# create food
food = Food()

# establish key listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# main game loop
game_is_on = True
while game_is_on:
    # print(scoreboard.message + str(scoreboard.score))

    # updates the screen after each move
    # placed outside of the move loop
    # prevents seeing each independent segment 
    # move individually
    screen.update()
    # delays the time cycle of 
    # each move by 0.1 second
    time.sleep(0.1)

    snake.move()

    # detect snake collision with food
    if snake.head.distance(food) < 20:
        # console test statement
        # print("Snake ate the food")
        
        # food respawns to new location
        food.refresh()
        # snake grows corresponding to food consumed
        snake.extend()
        # update scoreboard
        scoreboard.increase_score()

    # detect snake collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

    # detect collision of snake with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()