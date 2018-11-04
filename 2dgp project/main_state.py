import random
import game_world
import Unit_class
import game_framework
from pico2d import *
import cursor_class
import Unit_class

import game_framework
import title_state

player = None
background_image = None
def enter():
    global background_image
    background_image = load_image('resources\\TileMap\\Map.png')
    game_world.add_object(Unit_class.Observer(400,300),1)

def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global player
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            # 마우스 좌표 업데이트
            game_world.update_mouse_point(event.x, event.y)

        elif event.type == SDL_MOUSEBUTTONDOWN:
           pass



def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    global background_image
    clear_canvas()
    background_image.clip_draw(game_world.screen_x, game_world.screen_y, 800,600, 800/2, 600/2)

    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()






