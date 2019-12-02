import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1800-1), random.randint(0, 1100)

    def get_bb(self):
        return 0,0,0,0

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

