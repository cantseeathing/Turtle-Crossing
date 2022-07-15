from turtle import Turtle


class Score:
    def __init__(self, screen_size):
        self.game_over_banner = Turtle()
        self.game_over_banner.hideturtle()
        self.game_over_banner.penup()
        self.game_over_banner.color('red')
        self.level = 1
        self.screen_size = screen_size
        self.score_banner_object = Turtle()
        self.score_banner_object.color("green")
        self.score_banner_object.penup()
        self.score_banner_object.hideturtle()
        self.score_banner_object.goto(x=int((self.screen_size[0] / -2) * 0.95), y=int((self.screen_size[1] / 2) * 0.87))
        self.score_banner_object.write(f"Level: {self.level}", True, align="left",
                                       font=('Arial', 15, 'normal'))
        self.high_score = 0

    def game_over(self):
        self.game_over_banner.write("Game Over!", True, align="center", font=('Arial', 15, 'bold'))

    def update_score(self):
        self.level += 1
        self.score_banner_object.clear()
        self.score_banner_object.goto(x=int((self.screen_size[0] / -2) * 0.95), y=int((self.screen_size[1] / 2) * 0.87))
        self.score_banner_object.write(f"Level: {self.level}", True, align="left",
                                       font=('Arial', 15, 'normal'))
