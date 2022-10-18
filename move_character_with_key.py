from pico2d import *
import game_framework
import title_state

map1_WIDTH, map1_HEIGHT = 600, 600


def handle_events():
    global running
    global dir
    global uir
    global bottom
    global x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                dir -= 1
                bottom =80
            elif event.key == SDLK_RIGHT:
                dir += 1
                bottom = 0
            elif event.key == SDLK_UP:
                uir +=1
                bottom=160
            elif event.key == SDLK_DOWN:
                uir -=1
                bottom=240
            elif event.key == SDLK_SPACE:
                bomb = load_image('bomb1.png')
                bomb.draw(x,y)
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type ==SDL_KEYUP:
            if event.key ==SDLK_LEFT:
                dir +=1
            elif event.key == SDLK_RIGHT:
                dir -=1
            elif event.key == SDLK_UP:
                uir -=1
            elif event.key == SDLK_DOWN:
                uir+=1
    pass





open_canvas(map1_WIDTH, map1_HEIGHT)
map1_ground = load_image('map1.png')
character = load_image('bazzie_move.png')


running = True


x = map1_WIDTH // 2
y = map1_HEIGHT//2
frame = 0
dir = 0
uir = 0
bottom = 80

while running:
    clear_canvas()
    map1_ground.draw(300, 300)
    character.clip_draw(frame * 80, bottom, 80, 80, x, y)
    update_canvas()
    handle_events()

    frame = (frame + 1) %8

    x+= dir*5
    if(x==10):
        x+=5
    if(x==map1_WIDTH-10):
        x-=5
    y += uir*5
    if (y == 10):
        y += 5
    if (y == map1_HEIGHT - 10):
        y -= 5
    delay(0.01)


close_canvas()

