import turtle
from turtle import Turtle, Screen
import time
import Score_board


class Player:
    def __init__(self, screen_size, time_delay, turtle_increments):
        self.most_upper_bounds = None
        self.turtle_increments = turtle_increments
        self.l_line = None
        self.upper_lines = None
        self.lower_lines = None
        self.middle_bounds = None
        self.lower_bounds = None
        self.upper_bounds = None
        self.time_delay = time_delay
        self.screen = Screen()
        self.screen_size = screen_size
        self.screen.bgcolor("white")
        self.screen.title("Turtle Cross v1.0")
        self.screen.setup(width=screen_size[0], height=screen_size[1])
        self.screen.tracer(0)
        self.time_delay = time_delay
        self.screen_size = screen_size
        self.player = None
        self.bounds()
        self.mid_lines_lower()
        self.mid_lines_higher()
        self.create_player_turtle()
        self.screen_update()

    def create_player_turtle(self):
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.color("black", "pink")
        self.player.penup()
        self.player.setheading(90)
        self.player.goto(x=0, y=int((self.screen_size[1] / -2) * 0.9))

    def screen_update(self):
        time.sleep(self.time_delay)
        self.screen.update()

    def bounds(self):
        bounds_width = 10
        self.most_upper_bounds = Turtle()
        self.most_upper_bounds.penup()
        self.most_upper_bounds.shape("square")
        self.most_upper_bounds.color("black")
        self.most_upper_bounds.shapesize(stretch_wid=bounds_width / 20, stretch_len=int(self.screen_size[0] / 20))
        self.most_upper_bounds.goto(x=0, y=int((self.screen_size[1] / 2) * 0.8))

        self.upper_bounds = Turtle()
        self.upper_bounds.penup()
        self.upper_bounds.shape("square")
        self.upper_bounds.color("black")
        self.upper_bounds.shapesize(stretch_wid=bounds_width / 20, stretch_len=int(self.screen_size[0] / 20))
        self.upper_bounds.goto(x=0, y=int((self.screen_size[1] / 2) * 0.1))

        self.middle_bounds = Turtle()
        self.middle_bounds.penup()
        self.middle_bounds.shape("square")
        self.middle_bounds.color("black")
        self.middle_bounds.shapesize(stretch_wid=bounds_width / 20, stretch_len=int(self.screen_size[0] / 20))
        self.middle_bounds.goto(x=0, y=int((self.screen_size[1] / -2) * 0.1))

        self.lower_bounds = Turtle()
        self.lower_bounds.color("black")
        self.lower_bounds.shape("square")
        self.lower_bounds.penup()
        self.lower_bounds.goto(x=0, y=int((self.screen_size[1] / -2) * 0.8))
        self.lower_bounds.shapesize(stretch_wid=bounds_width / 20, stretch_len=int(self.screen_size[0] / 20))

    def mid_lines_lower(self):
        self.upper_lines = []
        self.lower_lines = []
        lines_length = 80
        lines_width = 25
        lines_buffer = 40
        ll_y = ((self.screen_size[1] / -2) * 0.8) + (((self.screen_size[1] / 2) * 0.7) / 2)
        pos = int(self.screen_size[0] / -2)
        for i in range(int(self.screen_size[0] / lines_length)):
            self.l_line = Turtle()
            self.l_line.penup()
            self.l_line.shape("square")
            self.l_line.shapesize(stretch_wid=int(lines_width / 20), stretch_len=int(lines_length / 20))
            self.l_line.color("black")
            self.l_line.goto(x=pos - lines_length, y=ll_y)
            self.lower_lines.append(self.l_line)
            pos += (lines_length + lines_buffer)

    def mid_lines_higher(self):
        self.upper_lines = []
        self.lower_lines = []
        lines_length = 80
        lines_width = 25
        lines_buffer = 40
        ll_y = int(((self.screen_size[1] / 2) * 0.55) - ((self.screen_size[1] / 2) * 0.2) / 2)
        pos = int(self.screen_size[0] / -2)
        for i in range(int(self.screen_size[0] / lines_length)):
            self.l_line = Turtle()
            self.l_line.penup()
            self.l_line.shape("square")
            self.l_line.shapesize(stretch_wid=int(lines_width / 20), stretch_len=int(lines_length / 20))
            self.l_line.color("black")
            self.l_line.goto(x=pos - lines_length, y=ll_y)
            self.lower_lines.append(self.l_line)
            pos += (lines_length + lines_buffer)

    def player_move_up(self):
        self.player.forward(self.turtle_increments)
        self.screen_update()

    def player_move_down(self):
        new_y = self.player.ycor()
        if new_y > int(self.screen_size[1] / -2 * 0.9):
            self.player.backward(self.turtle_increments)
            self.screen_update()

    def player_move_right(self):
        new_x = self.player.xcor() + self.turtle_increments
        if new_x < int(self.screen_size[0] / 2):
            self.player.goto(x=new_x, y=self.player.ycor())
            self.screen_update()

    def player_move_left(self):
        new_x = self.player.xcor() - self.turtle_increments
        if new_x > int(self.screen_size[0] / -2):
            self.player.goto(x=self.player.xcor() - self.turtle_increments, y=self.player.ycor())
            self.screen_update()

    def player_position(self):
        return self.player.xcor(), self.player.ycor()

    def win_condition(self):
        if self.player.ycor() > self.most_upper_bounds.ycor():
            self.player.goto(x=0, y=int((self.screen_size[1] / -2) * 0.9))
            return True

    def game_lost(self):
        self.turtle_increments = 0
