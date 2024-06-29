from turtle import *
from player import Player
from cars import Cars
from score import Score
#from cartest import Cars
import time
from game_screen import GameScreen

Screen().tracer(0)
player = Player()
cars = Cars()
screen = GameScreen()
score = Score()


screen.screen.tracer(0)


#is_collide = []


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    cars.cars_move()
    screen.screen.update()


    #check collision
    #global is_collide
    #is_collide = cars.check_collision(player)

    #if is_collide[0]:
    if cars.check_collision(player):
        print("collision")
        screen.screen.update()
        score.player_won("LOOSE")
        game_is_on = False

    #check win
    if player.ycor() > 300:
        score.player_won("won")
        cars.increase_car_speed()
        player.player_reset()
    screen.screen.update()
    screen.screen.onkey(player.up, "Up")
    screen.screen.onkey(player.down, "Down")
#screen.screen.tracer(1)
#player.check_path(is_collide[1])
screen.screen.exitonclick()