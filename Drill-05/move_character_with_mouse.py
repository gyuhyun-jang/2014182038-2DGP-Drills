from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running, x, y, prev_x, prev_y, mouse_x, mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x,mouse_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            prev_x,prev_y = x,y
            x,y = event.x - 20,KPU_HEIGHT - 1 - event.y + 20

    pass

def line(x1,y1,x2,y2):
    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1-t)*x1+t*x2
        y = (1-t)*y1+t*y2


open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
Mouse = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
prev_x, prev_y, mouse_x, mouse_y = 0,0,0,0
frame = 0
hide_cursor()


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    Mouse.draw(mouse_x, mouse_y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




