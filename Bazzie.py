from pico2d import*

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

def handle_event(self,event):
    if event.type == SDL_KEYDOWN:
        match event.key:
            case pico2d.SDLK_LEFT:
                self.dir -= 1
            case pico2d.SDLK_RIGHT:
                self.dir += 1
            case pico2d.SDLK_UP:
                self.fir += 1
            case pico2d.SDLK_DOWN:
                self.fir -= 1


    elif event.type == SDL_KEYUP:
        match event.key:
            case pico2d.SDLK_LEFT:
                self.dir += 1
            case pico2d.SDLK_RIGHT:
                self.dir -= 1
            case pico2d.SDLK_UP:
                self.fir -= 1
            case pico2d.SDLK_DOWN:
                self.fir += 1

