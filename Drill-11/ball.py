import random
from pico2d import *
import game_world
import game_framework
import brick

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0
        self.dir = 0
        self.move_speed = 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
        # fill here
        return 0,0,0,0

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
        # fill here for draw

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time
        if self.dir != 0:
            self.x += self.move_speed * game_framework.frame_time
            if self.x >= 1510:
                self.move_speed = -200
            if self.x <= 90:
                self.move_speed = 200


    #fill here for def stop

    def stop(self):
        self.fall_speed = 0

    def ball_on_brick(self, brick):
        self.dir, self.move_speed = brick.dir, brick.move_speed





# fill here
# class BigBall
class BigBall(Ball):
    MIN_FALL_SPEED = 50
    MAX_FALL_SPEED = 200
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1600-1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED,
                                         BigBall.MAX_FALL_SPEED)
        self.dir, self.move_speed = 0, 0

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20