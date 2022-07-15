from turtle import Turtle
import random


class Cars:
    def __init__(self, screen_size, car_speed):
        self.screen_size = screen_size
        self.left_cars_list = []
        self.right_cars_list = []
        self.car_speed = car_speed
        self.colors = ["blue", "green", "purple", "yellow", "pink", "purple", "orange", "red"]
        self.car = None

    def create_cars(self, initial_cars):
        self.left_cars_list = []
        self.right_cars_list = []
        for i in range(initial_cars):
            self.car = Turtle()
            self.car.penup()
            self.car.shape("square")
            self.car.color(random.choice(self.colors))
            self.car.setheading(180)
            car_cord_x = random.randint(int(-self.screen_size[0] / 2), int(self.screen_size[0] / 2))
            car_cord_y = random.randint(int((self.screen_size[1] / -2) * 0.8 * 0.85),
                                        int((self.screen_size[1] / -2) * 0.25 * 0.9))
            self.car.goto(x=car_cord_x, y=car_cord_y)
            self.car.shapesize(stretch_wid=random.randint(1, 2), stretch_len=random.randint(1, 2))
            j = 0
            while j < len(self.left_cars_list) - 1:
                if self.car.distance(self.left_cars_list[j]) < 70:
                    car_cord_x = random.randint(int(-self.screen_size[0] / 2), int(self.screen_size[0] / 2))
                    car_cord_y = random.randint(int((self.screen_size[1] / -2) * 0.8 * 0.85),
                                                int((self.screen_size[1] / -2) * 0.25 * 0.9))
                    self.car.goto(x=car_cord_x, y=car_cord_y)
                    j = 0
                else:
                    j += 1
            self.left_cars_list.append(self.car)

        for i in range(initial_cars):
            self.car = Turtle()
            self.car.penup()
            self.car.shape("square")
            self.car.color(random.choice(self.colors))
            self.car.setheading(0)
            car_cord_x = random.randint(int(-self.screen_size[0] / 2), int(self.screen_size[0] / 2))
            car_cord_y = random.randint(int((self.screen_size[1] / 2) * 0.2),
                                        int(((self.screen_size[1] / 2) * 0.8 * 0.85)))
            self.car.goto(x=car_cord_x, y=car_cord_y)
            self.car.shapesize(stretch_wid=random.randint(1, 2), stretch_len=random.randint(1, 2))
            j = 0
            while j < len(self.right_cars_list) - 1:
                if self.car.distance(self.right_cars_list[j]) < 70:
                    car_cord_x = random.randint(int(-self.screen_size[0] / 2), int(self.screen_size[0] / 2))
                    car_cord_y = random.randint(int((self.screen_size[1] / 2) * 0.2),
                                                int(((self.screen_size[1] / 2) * 0.8 * 0.85)))
                    self.car.goto(x=car_cord_x, y=car_cord_y)
                    j = 0
                else:
                    j += 1
            self.right_cars_list.append(self.car)

    def move_cars(self, car_speed):
        for i in range(len(self.left_cars_list)):
            self.left_cars_list[i].forward(car_speed)
        for i in range(len(self.right_cars_list)):
            self.right_cars_list[i].forward(car_speed)
        for i in range(len(self.left_cars_list)):
            if self.left_cars_list[i].xcor() < self.screen_size[0] / -2:
                self.left_cars_list[i].goto(x=int((self.screen_size[0] / 2)), y=self.left_cars_list[i].ycor())
        for i in range(len(self.right_cars_list)):
            if self.right_cars_list[i].xcor() > self.screen_size[0] / 2:
                self.right_cars_list[i].goto(x=int((self.screen_size[0] / -2)), y=self.right_cars_list[i].ycor())

    def check_collision(self, player_pos, player):
        car_distance = 25
        player_pos_x = player.xcor()
        player_pos_y = player.ycor()
        threshold = 3
        crash = False
        if player_pos_y < 0:
            for i in range(len(self.left_cars_list)):
                if self.left_cars_list[i].distance(player) < car_distance and \
                        (self.left_cars_list[i].ycor() <= player.ycor() - threshold or
                         self.left_cars_list[i].ycor() >= player.ycor() + threshold):
                    crash = True
        else:
            for i in range(len(self.right_cars_list)):
                if self.right_cars_list[i].distance(player) < car_distance and \
                        (self.right_cars_list[i].ycor() <= player.ycor() - threshold or
                         self.right_cars_list[i].ycor() >= player.ycor() + threshold):
                    crash = True
        return crash

    def remove_cars(self):
        for i in range(len(self.left_cars_list)):
            self.left_cars_list[i].hideturtle()
            self.left_cars_list[i].clear()
        for i in range(len(self.right_cars_list)):
            self.right_cars_list[i].hideturtle()
            self.right_cars_list[i].clear()
        self.left_cars_list = []
        self.right_cars_list = []
