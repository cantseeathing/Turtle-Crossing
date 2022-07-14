import player
import Score_board
import cars

SCREEN_SIZE = (800, 600)
TIME_DELAY = 0.001
TURTLE_INCREMENTS = 25
INITIAL_CARS = 1
CAR_SPEED = 1
GAME_ON = True

player_object = player.Player(screen_size=SCREEN_SIZE, time_delay=TIME_DELAY, turtle_increments=TURTLE_INCREMENTS)
score = Score_board.Score(screen_size=SCREEN_SIZE)
car_objects = cars.Cars(screen_size=SCREEN_SIZE, car_speed=CAR_SPEED)
car_objects.create_cars(initial_cars=INITIAL_CARS)
player_object.screen_update()

player_object.screen.listen()
player_object.screen.onkey(key="a", fun=player_object.player_move_left)
player_object.screen.onkey(key="d", fun=player_object.player_move_right)
player_object.screen.onkey(key="w", fun=player_object.player_move_up)
player_object.screen.onkey(key="s", fun=player_object.player_move_down)


while GAME_ON:
    crash = car_objects.check_collision(player_object.player_position(), player_object.player)
    if crash:
        score.game_over()
        player_object.game_lost()
        GAME_ON = False
    else:
        car_objects.move_cars()
        win = player_object.win_condition()
        if win:
            score.update_score()
            car_objects.remove_cars()
            player_object.screen_update()
            CAR_SPEED += 1
            INITIAL_CARS += 1
            car_objects.create_cars(initial_cars=INITIAL_CARS)
        player_object.screen_update()

player_object.screen.exitonclick()
