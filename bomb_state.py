from pico2d import *
import game_framework
import play_state
import title_state

# fill here
#running = True
image = None
count = 1

def enter():
    global image
    image = load_image('bomb_ready.png')

def exit():
    global image
    del image

def update():
    play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,400)

    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_SPACE:
                    play_state.boy.item = 'bomb_ready'
                    game_framework.pop_state()


