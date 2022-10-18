from pico2d import *
import random
import game_framework

import title_state


team = None
grass = None

class Map1:
    def __init__(self):
        self.image = load_image('map1.png')

    def draw(self):
        self.image.draw(400, 300)

class Bazzie:
    def __init__(self):
        self.x, self.y = 0,90
        self.frame = 0
        self.dir = 1
        self.image = load_image('bazzie_move.png')


    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir*1
        if self.x> 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x=0
            self.dir = 1

    def draw(self):
        if self.dir ==1:
            self.image.clip_draw(self.frame*80, 0, 80, 80, self.x, self.y)
        elif self.dir ==-1:
            self.image.clip_draw(self.frame*80, 80, 80, 80, self.x, self.y)

        delay(0.001)

def handle_events():
    #global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            # running = False
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)





#초기화
def enter():
    global bazzie, map1
    bazzie = Bazzie()
    map1 = Map1()



#종료
def exit():
    global bazzie,map1
    del bazzie
    del map1

# 월드에 존재하는 객체들을 업데이트
def update():
    bazzie.update()
    # grass는 움직이지 않기에 업데이트가 필요없기에 생략

#월드를 그린다.
def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    map1.draw()
    bazzie.draw()



def pause():
    pass

def resume():
    pass




