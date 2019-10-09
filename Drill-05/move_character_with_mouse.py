from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x,y
    global mouse_x,mouse_y
    global save_x,save_y
    global move_ani
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running =False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x+20, KPU_HEIGHT - 1 - event.y-10
        elif event.type ==SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            save_x,save_y = x,y
            x, y = event.x, KPU_HEIGHT - 1 - event.y
            move_ani =300

        elif event.type ==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            running =False



open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
Mouse = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mouse_x, mouse_y =0,0
frame = 0
move_ani=300
save_x,save_y=KPU_WIDTH // 2, KPU_HEIGHT // 2
hide_cursor()

def run():
    global  x,y
    global save_x,save_y
    global running
    frame=0
    count = 0
    while count<10:
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        Mouse.draw(mouse_x, mouse_y)
        divine_x = (-x + save_x) / 10
        divine_y = (-y + save_y) / 10
        x = x + divine_x
        y = y + divine_y
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        move_ani =300
        count+=1
        if(count == 10):
            count=0
            running=False



while running:

    run()
    handle_events()

close_canvas()




