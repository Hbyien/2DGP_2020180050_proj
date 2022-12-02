from pico2d import*
import game_framework
import title_state


bazzie = None
map = None
running = None

class Map:
    def __init__(self):
        self.image = load_image('map.png')
    def draw(self):
        self.image.draw(400,400)

class Bomb:
    def __init__(self):
        self.image = load_image('bomb_ready.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir * 1
        self.y += self.fir * 1


    def draw(self):
        self.bomb_ready_image.clip_draw(self.frame * 37, 0, 37, 50, self.x, self.y)


class Bazzie:
    image = None
    def __init__(self):
        self.x, self.y = 0,90
        self.frame = 0
        self.dir , self.fir= 0, 0
        if Bazzie.image == None:
            Bazzie.image = load_image('bazzie_move.png')
        self.bomb_ready_image=load_image('bomb_ready.png')
        self.item = None

    def update(self):
        self.frame = (self.frame+1) % 8
        self.x += self.dir*1
        self.y += self.fir*1
        self.x = clamp(0,self.x,800)
        self.y = clamp(0,self.y,800)

    def draw(self):
        self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)
        if self.dir == 1:
            self.image.clip_draw(self.frame*80,0,80,80,self.x,self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 80, 80, 80, 80, self.x, self.y)
        elif self.fir == 1:
            self.image.clip_draw(self.frame * 80, 160, 80, 80, self.x, self.y)
        elif self.fir == -1:
            self.image.clip_draw(self.frame * 80, 240, 80, 80, self.x, self.y)



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.change_state(title_state)
                case pico2d.SDLK_LEFT:
                    bazzie.dir -= 1
                case pico2d.SDLK_RIGHT:
                    bazzie.dir += 1
                case pico2d.SDLK_UP:
                    bazzie.fir+=1
                case pico2d.SDLK_DOWN:
                    bazzie.fir-=1
                case pico2d.SDLK_SPACE:
                    bazzie.item = 'bomb_ready'
        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_LEFT:
                    bazzie.dir += 1
                case pico2d.SDLK_RIGHT:
                    bazzie.dir -= 1
                case pico2d.SDLK_UP:
                    bazzie.fir -= 1
                case pico2d.SDLK_DOWN:
                    bazzie.fir += 1



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

def draw_world():
    map.draw()
    bazzie.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()





def pause():
    pass
def resume():
    pass
