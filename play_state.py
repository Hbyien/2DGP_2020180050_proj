from pico2d import*
import game_framework

bazzie = None
map = None
running = None

class Map:
    def __init__(self):
        self.image = load_image('map1.png')
    def draw(self):
        self.image.draw(400,30)
class Bazzie:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('bazzie_move.png')


    def update(self):
        self.frame = (self.frame+1) % 8
        self.x += self.dir*2
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*80,0,80,80,self.x,self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 80, 80, 80, 80, self.x, self.y)
        delay(0.001)


def handle_events():
    global dir
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        #  elif event.type==SDL_KEYDOWN:
        #      if event.key==SDLK_RIGHT:
        #          dir+=1
        #      elif event.key == SDLK_LEFT:
        #          dir-=1
        #     elif event.key ==SDLK_ESCAPE:
        #         game_framework.quit()
        # elif event.type == SDL_KEYUP:
        #     if event.key==SDLK_RIGHT:
        #         dir-=1
        #     elif event.key==SDLK_LEFT:
        #         dir+=1
def enter():
    global bazzie, map, running
    bazzie = Bazzie()
    map = Map()
    running = True

def exit():
    global bazzie, map
    del bazzie
    del map

def update():
    bazzie.update()

def draw():
    clear_canvas()
    map.draw()
    bazzie.draw()
    update_canvas()




