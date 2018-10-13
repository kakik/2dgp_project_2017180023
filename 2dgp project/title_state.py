import game_framework
import difficulty_selection_state
import IMG_class
import cursor_class
from pico2d import *

name = "TitleState"

# 이미지 파일
Title_BG_img = None
Title_start_img, Title_start_mouse_on_img = None, None
Title_exit_img, Title_exit_mouse_on_img = None, None
Title_start_text_img, Title_exit_text_img = None, None

# 이미지별 최대 프레임
Title_start_img_max_frame = 35
Title_start_mouse_on_img_max_frame = 60
Title_exit_img_max_frame = 50
Title_exit_mouse_on_img_max_frame = 30

# 이미지 객체
Title_start = None
Title_start_mouse_on = None
Title_exit = None
Title_exit_mouse_on = None


def enter():
    global Title_BG_img
    global Title_start_img, Title_start_mouse_on_img
    global Title_exit_img, Title_exit_mouse_on_img
    global Title_start_text_img, Title_exit_text_img
    global Title_start, Title_start_mouse_on
    global Title_exit, Title_exit_mouse_on

    # 초기 마우스 좌표
    cursor_class.mx = 800/2
    cursor_class.my = 600/2

    # 객체 생성! 출력 좌표, 이미지 사이즈 조정은 여기서
    Title_start = IMG_class.MenuIMG(240, 438, 320, 116, Title_start_img_max_frame, 4, 1)
    Title_start_mouse_on = IMG_class.MenuMouseOnIMG(240, 438, 320, 116, Title_start_mouse_on_img_max_frame, 4, 1)
    Title_exit = IMG_class.MenuIMG(592, 122, 184, 128, Title_exit_img_max_frame, 4, 2)
    Title_exit_mouse_on = IMG_class.MenuMouseOnIMG(592, 122, 184, 128, Title_exit_mouse_on_img_max_frame, 4, 2)

    # 메뉴 이미지 로드
    Title_BG_img = load_image('resources\\Title\\Background\\Title_BG.png')
    Title_start_img = [load_image('resources\\Title\\Start\\single%d%d.png'%(i//10, i%10)) for i in range(0, Title_start_img_max_frame)]
    Title_start_mouse_on_img = [load_image('resources\\Title\\Start\\English\\singleon%d%d.png'%(i//10, i%10)) for i in range(0, Title_start_mouse_on_img_max_frame)]
    Title_exit_img = [load_image('resources\\Title\\Exit\\exit%d%d.png'%(i//10, i%10)) for i in range(0, Title_exit_img_max_frame)]
    Title_exit_mouse_on_img = [load_image('resources\\Title\\Exit\\English\\exiton%d%d.png'%(i//10, i%10)) for i in range(0, Title_exit_mouse_on_img_max_frame)]
    Title_start_text_img = load_image('resources\\Title\\Start\\start.png')
    Title_exit_text_img = load_image('resources\\Title\\Exit\\exit.png')

    # 커서 이미지 로드
    cursor_class.Cursor_img = load_image('resources\\Cursor\\cursor.png')

def exit():
    global Title_BG_img
    global Title_start_img, Title_start_mouse_on_img
    global Title_exit_img, Title_exit_mouse_on_img

    del Title_BG_img
    del Title_start_img, Title_start_mouse_on_img
    del Title_exit_img, Title_exit_mouse_on_img


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






