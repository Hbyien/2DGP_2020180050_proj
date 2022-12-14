from pico2d import *
import game_framework
import title_state


image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('start_logo.png')



def exit():
    global image
    del image


def update():
    global logo_time
    #global running
    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(title_state)

    delay(0.01)
    logo_time += 0.01


def draw():
    clear_canvas()
    image.draw(400,400)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()