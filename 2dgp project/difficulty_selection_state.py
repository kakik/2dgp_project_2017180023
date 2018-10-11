from pico2d import *

import game_framework
import title_state

Difficulty_BG_img = None
mx, my = 0, 0

def enter():
    global Difficulty_BG_img
    Difficulty_BG_img = load_image('resources\\Title\\Background\\Title_BG.png')

def exit():
    del Difficulty_BG_img


def pause():
    pass


def resume():
    pass


def handle_events():
    global mx, my
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            if event.key == SDLK_ESCAPE:
                game_framework.quit()


def update():
    pass


def draw():
    global mx, my
    clear_canvas()

    Difficulty_BG_img.draw(400, 300)

    update_canvas()
    delay(0.05)








