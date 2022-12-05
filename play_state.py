from pico2d import*
import game_framework
import game_world
import title_state
from map import Map
from bazzie import Bazzie

bazzie = None
map = None
running = None



# class Bomb:
#     def __init__(self):
#         self.image = load_image('bomb_ready.png')
#
#     def update(self):
#         self.frame = (self.frame + 1) % 4
#         self.x += self.dir * 1
#         self.y += self.fir * 1
#
#
#     def draw(self):
#         self.bomb_ready_image.clip_draw(self.frame * 37, 0, 37, 50, self.x, self.y)
#




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            else:
                bazzie.handle_event(event)




def enter():
    global bazzie, map, running
    bazzie = Bazzie()
    map = Map()
    game_world.add_object(map, 0)
    game_world.add_object(bazzie,1)


def exit():
   game_world.clear()
def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()





def pause():
    pass
def resume():
    pass
