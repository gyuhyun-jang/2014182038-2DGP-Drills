from pico2d import *
import game_framework
import game_world

class Brick:
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y, self.move_speed = 1000, 180, 200
        self.dir = 1

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.move_speed * game_framework.frame_time
        if self.x >= 1510:
            self.move_speed = -200
        if self.x <= 90:
            self.move_speed = 200

