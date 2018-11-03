from pico2d import *
import cursor_class
import game_framework
import game_world
import Unit_class


name = "DifficultySelectionState"

Difficulty_BG_img = None
mx, my = 0, 0

observer = None
wraith = None
scourge = None
def enter():
    global Difficulty_BG_img
    global observer,wraith, scourge

    Difficulty_BG_img = load_image('resources\\Title\\Background\\Title_BG.png')

    observer = Unit_class.Observer(400, 300)
    wraith = Unit_class.Wraith(200, 300)
    scourge = Unit_class.Scourge(600, 300)

    game_world.add_object(observer, 1)
    game_world.add_object(wraith, 1)
    game_world.add_object(scourge, 1)

def exit():
    del Difficulty_BG_img
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            # 마우스 좌표 업데이트
            cursor_class.update_mouse_point(event.x, event.y)

        elif event.type == SDL_MOUSEBUTTONDOWN:
            pass


def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()

    if Difficulty_BG_img != None:
        Difficulty_BG_img.draw(800/2, 600/2)

    for game_object in game_world.all_objects():
        game_object.draw()


    update_canvas()







