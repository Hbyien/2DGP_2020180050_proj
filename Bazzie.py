from pico2d import*

class Map:
    def __init__(self):
        self.image = load_image('map1.png')
    def draw(self):
        self.image.draw(400,30)

class Bazzie:
    def __init__(self):
        self.x, self.y = 0,90
        self.frame=0
        self.image = load_image('bazzie_move.png')

    def update(self):
        self.frame = (self.frame+1)%8
        self.x+=self.dir*5

    def draw(self):
        self.image.clip_draw(self.frame*80,0,80,80,self.x,self.y)


def handle_events():
    global running
    global dir
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            running=False
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                dir+=1
            elif event.key == SDLK_LEFT:
                dir-=1
            elif event.key ==SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                dir-=1
            elif event.key==SDLK_LEFT:
                dir+=1

    pass

open_canvas()

map=Map()
bazzie=Bazzie()

running = True

while running:
    handle_events()
    bazzie.update()
    clear_canvas()
    map.draw()
    bazzie.draw()
    update_canvas()

    delay(0.05)


del bazzie
del map



close_canvas()