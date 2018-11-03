import game_framework
import difficulty_selection_state
import IMG_class
import cursor_class
import game_world
from pico2d import *

name = "TitleState"

# 이미지 파일
Title_BG_img = None

# 이미지 객체
Title_start = None
Title_start_mouse_on = None
Title_exit = None
Title_exit_mouse_on = None
#커서
cursor = None

def enter():
    global Title_BG_img
    global Title_start_text_img, Title_exit_text_img
    global Title_start, Title_start_mouse_on
    global Title_exit, Title_exit_mouse_on

    # 초기 마우스 좌표
    cursor_class.mx = 800/2
    cursor_class.my = 600/2
    Title_BG_img = load_image('resources\\Background\\Title_BG.png')

    # 객체 생성!
    Title_start = IMG_class.MenuStartIMG()
    Title_start_mouse_on =IMG_class.MenuStartMouseOnIMG()
    Title_exit = IMG_class.MenuExitIMG()
    Title_exit_mouse_on = IMG_class.MenuExitMouseOnIMG()
    cursor = cursor_class.Cursor()

    game_world.add_object(Title_start)
    game_world.add_object(Title_start_mouse_on)
    game_world.add_object(Title_exit)
    game_world.add_object(Title_exit_mouse_on)
    game_world.add_object(Title_start)
    game_world.add_object(cursor)

def exit():
    game_world.clear()

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

            # start, quit 메뉴 - 마우스 충돌체크
            Title_start.handle_events()
            Title_start_mouse_on.handle_events()
            Title_exit.handle_events()
            Title_exit_mouse_on.handle_events()

        elif event.type == SDL_MOUSEBUTTONDOWN:
            # 게임 시작
            if Title_start.mouse_on:

                game_framework.change_state(difficulty_selection_state)
            # 게임 종료
            elif Title_exit.mouse_on:
                game_framework.quit()


def update():
    pass


def draw():
    clear_canvas()

    Title_BG_img.draw(400, 300)
    Title_start_mouse_on.draw()
    Title_start.draw()
    Title_exit.draw()
    Title_exit_mouse_on.draw()
    Title_start_text_img.draw(200, 480)
    Title_exit_text_img.draw(550, 180)
    cursor_class.cursor.draw()

    update_canvas()
    delay(0.01)


def pause():
    pass


def resume():
    pass






