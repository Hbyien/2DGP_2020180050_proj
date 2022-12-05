from pico2d import*

import game_framework
import game_world
from bomb import Bomb

PIXEL_PER_METER=(10.0/0.3)
RUN_SPEED_KMPH  = 20.0 # Km / Hour
RUN_SPEED_MPM   = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS   = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS   = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8




RD, LD,UD,DD, RU, LU,UU,DU,SPACE= range(9)

event_name = ['RD', 'LD','UD','DD','RU','LU','UU','DU','SPACE']
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYDOWN,SDLK_UP): UD,
    (SDL_KEYDOWN,SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYUP, SDLK_UP) : UU,
    (SDL_KEYUP, SDLK_DOWN) : DU,
    (SDL_KEYDOWN,SDLK_SPACE) : SPACE
}

class IDLE:
    @staticmethod
    def enter(self,event):
        self.dir=0
        self.fir=0

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
        if event == SPACE:
            self.bomb()
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)%8

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(int(self.frame) * 80, 0, 80, 80, self.x, self.y)
        elif self.face_dir == -1:
            self.image.clip_draw(int(self.frame) * 80, 80, 80, 80, self.x, self.y)
        elif self.face_fir == 1:
            self.image.clip_draw(int(self.frame) * 80, 160, 80, 80, self.x, self.y)
        elif self.face_fir == -1:
            self.image.clip_draw(int(self.frame) * 80, 240, 80, 80, self.x, self.y)


class RUN:
    @staticmethod
    def enter(self,event):
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == UD:
            self.fir += 1
        elif event == DD:
            self.fir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        elif event == UU:
            self.fir -= 1
        elif event == DU:
            self.fir += 1


    @staticmethod
    def exit(self, event):
        self.face_dir = self.dir
        self.face_fir = self.fir
        if event == SPACE:
            self.bomb()


    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)%8
        self.x += self.dir*RUN_SPEED_PPS* game_framework.frame_time
        self.y += self.fir*RUN_SPEED_PPS* game_framework.frame_time
        self.x = clamp(0,self.x,800)
        self.y = clamp(0,self.y,800)

    @staticmethod
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame)*80,0,80,80,self.x,self.y)
        elif self.dir == -1:
            self.image.clip_draw(int(self.frame) * 80, 80, 80, 80, self.x, self.y)
        elif self.fir == 1:
            self.image.clip_draw(int(self.frame) * 80, 160, 80, 80, self.x, self.y)
        elif self.fir == -1:
            self.image.clip_draw(int(self.frame) * 80, 240, 80, 80, self.x, self.y)

        pass

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN,UU:RUN, DU:RUN,UD:RUN,DD:RUN, SPACE: IDLE },
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE,UU:IDLE, DU:IDLE,UD:IDLE,DD:IDLE , SPACE: RUN}
}

class Bazzie:
    image = None
    def __init__(self):
        self.x, self.y = 800//2,90
        self.frame = 0
        self.dir , self.fir= 0, 0
        self.face_dir,self.face_fir= 1,1
        if Bazzie.image == None:
            Bazzie.image = load_image('bazzie_move.png')
        self.event_que =[]
        self.cur_state=IDLE
        self.cur_state.enter(self,None)

    def update(self):
        self.cur_state.do(self)
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self,event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__} Event{event_name[event]}')
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir}, Dir: {self.dir}')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def bomb(self):
        bomb = Bomb(self.x,self.y,self.face_dir*2, self.face_fir*2)
        game_world.add_object(bomb, 1)
        print('Bomb')

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
    #                 self.face_dir = -1
    #             case pico2d.SDLK_RIGHT:
    #                 self.dir -= 1
    #                 self.face_dir =1
    #             case pico2d.SDLK_UP:
    #                 self.fir -= 1
    #                 self.face_fir =1
    #             case pico2d.SDLK_DOWN:
    #                 self.fir += 1
    #                 self.face_fir = -1
    #
