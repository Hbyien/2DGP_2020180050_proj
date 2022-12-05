from pico2d import*



RD, LD,UD,DD, RU, LU,UU,DU = range(8)
#키입력을 단순화 시켜서 이벤트로 해석
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYDOWN,SDLK_UP): UD,
    (SDL_KEYDOWN,SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYUP, SDLK_UP) : UU,
    (SDL_KEYUP, SDLK_DOWN) : DU
}

class Bazzie:
    image = None
    def __init__(self):
        self.x, self.y = 0,90
        self.frame = 0
        self.dir , self.fir= 0, 0
        if Bazzie.image == None:
            Bazzie.image = load_image('bazzie_move.png')
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self,None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    #
    # def update(self):
    #     self.cur_state.d0(self)
    #     self.frame = (self.frame+1) % 8
    #     self.x += self.dir*1
    #     self.y += self.fir*1
    #     self.x = clamp(0,self.x,800)
    #     self.y = clamp(0,self.y,800)
    #
    # def draw(self):
    #     self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)
    #     if self.dir == 1:
    #         self.image.clip_draw(self.frame*80,0,80,80,self.x,self.y)
    #     elif self.dir == -1:
    #         self.image.clip_draw(self.frame * 80, 80, 80, 80, self.x, self.y)
    #     elif self.fir == 1:
    #         self.image.clip_draw(self.frame * 80, 160, 80, 80, self.x, self.y)
    #     elif self.fir == -1:
    #         self.image.clip_draw(self.frame * 80, 240, 80, 80, self.x, self.y)

# def handle_event(self,event):
#     if event.type == SDL_KEYDOWN:
#         match event.key:
#             case pico2d.SDLK_LEFT:
#                 self.dir -= 1
#             case pico2d.SDLK_RIGHT:
#                 self.dir += 1
#             case pico2d.SDLK_UP:
#                 self.fir += 1
#             case pico2d.SDLK_DOWN:
#                 self.fir -= 1
#     elif event.type == SDL_KEYUP:
#         match event.key:
#             case pico2d.SDLK_LEFT:
#                 self.dir += 1
#             case pico2d.SDLK_RIGHT:
#                 self.dir -= 1
#             case pico2d.SDLK_UP:
#                 self.fir -= 1
#             case pico2d.SDLK_DOWN:
#                 self.fir += 1

class IDLE:

    def enter(self,event):
        self.dir=0
        self.fir=0
        pass


    def exit(self):
        pass


    def do(self):
        self.frame = (self.frame+1)%8
        pass


    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*80,0,80,80,self.x,self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 80, 80, 80, 80, self.x, self.y)
        elif self.fir == 1:
             self.image.clip_draw(self.frame * 80, 160, 80, 80, self.x, self.y)
        elif self.fir == -1:
             self.image.clip_draw(self.frame * 80, 240, 80, 80, self.x, self.y)
        pass



class RUN:
    def enter(self,event):
        if event == RD:
            self.dir +=1
        elif event ==LD:
            self.dir -=1
        elif event ==RU:
            self.dir -=1
        elif event == LU:
            self.dir +=1
        elif event == UD:
            self.fir +=1
        elif event == DD:
            self.fir-=1
        elif event ==UU:
            self.fir-=1
        elif event==DU:
            self.fir+=1



    def exit(self):

        pass


    def do(self):
        self.frame = (self.frame + 1) % 8

        self.x += self.dir
        self.y += self.fir
        self.x = clamp(0, self.x, 800)
        self.y = clamp(0, self.y, 800)




  def draw(self):
      if self.dir == 1:
          self.image.clip_draw(self.frame * 80, 0, 80, 80, self.x, self.y)
      elif self.dir == -1:
          self.image.clip_draw(self.frame * 80, 80, 80, 80, self.x, self.y)
      elif self.fir == 1:
          self.image.clip_draw(self.frame * 80, 160, 80, 80, self.x, self.y)
      elif self.fir == -1:
          self.image.clip_draw(self.frame * 80, 240, 80, 80, self.x, self.y)

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN,UU:RUN, DU:RUN,UD:RUN,DD:RUN },
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE,UU:IDLE, DU:IDLE,UD:IDLE,DD:IDLE}
}
