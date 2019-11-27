import game_framework
from pico2d import *

# 1 pixel 1cm
# 새의 크기 (150, 130)pixel = (150, 130) cm
# 새의 속도 20 km/h == 555pps
PIXEL_PER_METER = (10.0 / 0.1)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# 새의 날개짓 초당 2번
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    def __init__(self):
        self.x, self.y = 1600 // 2, 300
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frame = 0
        self.frame_XY = [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2],
                         [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
                         [0, 0], [1, 0], [2, 0], [3, 0]]

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame_XY[int(self.frame)][0] * 183,
                                 self.frame_XY[int(self.frame)][1] * 168, 180, 165, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_composite_draw(self.frame_XY[int(self.frame)][0] * 183,
                                           self.frame_XY[int(self.frame)][1] * 168, 180, 165, 0, 'h', self.x, self.y,
                                           180, 165)
        self.font.draw(self.x - 70, self.y + 70, '(Time: %3.2f)' % get_time(), (0, 0, 0))

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity * game_framework.frame_time
        if self.x >= 1510:
            self.velocity = -RUN_SPEED_PPS
        elif self.x <= 90:
            self.velocity = RUN_SPEED_PPS
        self.dir = clamp(-1, self.velocity, 1)
