from pico2d import *
import cursor_class
import game_framework
import game_world
import Unit_class
import main_state

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

    scourge = Unit_class.Scourge(200, 300)
    observer = Unit_class.Observer(400, 300)
    wraith = Unit_class.Wraith(600, 300)

    game_world.add_object(scourge, 1)
    game_world.add_object(observer, 1)
    game_world.add_object(wraith, 1)


def exit():
    global Difficulty_BG_img
    del Difficulty_BG_img
    # game_world.clear()
    game_world.remove_object(scourge)
    game_world.remove_object(observer)
    game_world.remove_object(wraith)

def pause():
    pass


def resume():
    pass


def handle_events():
    global observer, wraith, scourge
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
            if scourge.x-scourge.width/2 < cursor_class.mx <scourge.x+scourge.width/2 and scourge.y-scourge.height/2 < cursor_class.my <scourge.y+scourge.height/2:
                pass
            elif observer.x - observer.width / 2 < cursor_class.mx < observer.x + observer.width / 2 and observer.y - observer.height / 2 < cursor_class.my < observer.y + observer.height / 2:
                pass
            elif wraith.x - wraith.width / 2 < cursor_class.mx < wraith.x + wraith.width / 2 and wraith.y - wraith.height / 2 < cursor_class.my < wraith.y + wraith.height / 2:
                game_framework.change_state(main_state)


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







