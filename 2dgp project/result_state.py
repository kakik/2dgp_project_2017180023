import game_world
from pico2d import *
import game_framework
import main_state

name = "ResultState"

Result_BG_IMG = None

def enter():
    global Result_BG_IMG
    Result_BG_IMG = ResultBGIMG()
    game_world.add_object(Result_BG_IMG, 0)


def exit():
    pass

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

        if event.type == SDL_MOUSEMOTION:
                # 마우스 좌표 업데이트
                game_world.update_mouse_point(event.x, event.y)

def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()

def pause(): pass


def resume(): pass



class ResultBGIMG():
    image = None
    width = 800
    height = 600

    def __init__(self):
        if self.image == None:
            self.image = load_image('resources\\Title\\Background\\Title_BG.png')
            self.font =  load_font('font\\starcraft.TTF', 20)
            self.clear_stage = main_state.stage_level - 1

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        if self.image != None:
            self.image.clip_draw(0, 0, game_world.screen_x, game_world.screen_y, game_world.screen_x / 2, game_world.screen_y / 2)