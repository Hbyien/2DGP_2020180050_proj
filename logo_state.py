from pico2d import *

running = True
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('start_logo.png')
    pass


def exit():
    global image
    del image


def update():
    global logo_time
    global running
    if logo_time > 1.0:
        logo_time = 0
        running=False
    delay(0.01)
    logo_time += 0.01


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events = get_events()