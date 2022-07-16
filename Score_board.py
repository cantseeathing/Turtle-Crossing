from turtle import Turtle


class Score:
    def __init__(self, screen_size):
        self.content = None
        with open("high_score.txt", mode="r") as file:
            self.content = file.read()
            file.close()
            if self.content == '':
                file = open("high_score.txt", mode="w")
                self.content = 0
                file.write(str(self.content))
            else:
                self.high_score = int(self.content)
            print(f"high score: {self.content}")
        self.high_score = int(self.content)
        self.game_over_banner = Turtle()
        self.game_over_banner.hideturtle()
        self.game_over_banner.penup()
        self.game_over_banner.color('red')
        self.level = 0
        self.screen_size = screen_size
        self.score_banner_object = Turtle()
        self.score_banner_object.color("green")
        self.score_banner_object.penup()
        self.score_banner_object.hideturtle()
        self.score_banner_object.goto(x=int((self.screen_size[0] / -2) * 0.95), y=int((self.screen_size[1] / 2) * 0.87))
        self.score_banner_object.write(f"Level: {self.level}\tHigh score: {self.high_score}", True, align="left",
                                       font=('Arial', 15, 'normal'))

    def game_over(self):
        self.game_over_banner.write("Game Over!", True, align="center", font=('Arial', 15, 'bold'))
        if self.level > self.high_score:
            self.high_score = self.level
            self.record()
        self.level = 0

    def update_score(self):
        self.level += 1
        self.score_banner_object.clear()
        if self.level > self.high_score:
            self.high_score = self.level
            self.record()
        self.score_banner_object.goto(x=int((self.screen_size[0] / -2) * 0.95), y=int((self.screen_size[1] / 2) * 0.87))
        self.score_banner_object.write(f"Level: {self.level}\tHigh score: {self.high_score}", True, align="left",
                                       font=('Arial', 15, 'normal'))

    def record(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))
            file.close()
        # try:
        #     with open("high_score.txt") as file:
        #         self.content = file.read()
        # except OSError:
        #     file.write("high_score.txt")
