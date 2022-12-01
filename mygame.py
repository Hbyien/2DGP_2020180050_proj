import pico2d
import game_framework
# import logo_state
import play_state


pico2d.open_canvas(800,800)
game_framework.run(play_state)
pico2d.clear_canvas()
