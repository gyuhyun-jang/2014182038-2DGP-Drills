import game_framework
import main_state
from pico2d import*

name = "PauseState"
image = None

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.flicker = 0

    def update(self):
        self.flicker = (self.flicker + 1) % 2
        delay(0.1)

    def draw(self):
        if self.flicker == 0:
            self.image.clip_draw(250,250,400,400,400,300)



def enter():
    global image
    image = load_image('pause.png')
    image = Pause()

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.pop_state()

def draw():
    clear_canvas()
    image.draw()
    main_state.boy.draw()
    main_state.grass.draw()
    update_canvas()

def update():
    image.update()
    pass

def pause():
    pass

def resume():
    pass