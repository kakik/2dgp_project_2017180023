import game_framework
import main_state
import IMG_class
from pico2d import *

name = "TitleState"


Title_BG_img = None
Title_start_main_img, Title_start_mouse_on_img = None, None
Title_exit_main_img, Title_exit_mouse_on_img = None, None

Title_start_main_img_max_frame = 35
Title_start_mouse_on_img_max_frame = 60
Title_exit_main_img_max_frame = 50
Title_exit_mouse_on_img_max_frame = 30

# 이미지 객체
Title_start_img = None
Title_exit_img = None


# 마우스 좌표
mx = 0
my = 0


class TitleStartImg(IMG_class.IMG):
    def __init__(self, x1, y1, x2, y2):
        super(TitleStartImg, self).__init__(x1, y1, x2, y2, 0, Title_start_main_img_max_frame)
        self.mouse_on_img_frame = 0
        self.mouse_on_img_max_frame = Title_start_mouse_on_img_max_frame
        self.mouse_on_img_on = False

    def draw(self):
        super(TitleStartImg, self).draw()

        if self.mouse_on_img_on == True:
            Title_start_mouse_on_img[self.mouse_on_img_frame].draw(self.x, self.y-60)
        Title_start_main_img[self.frame].draw(self.x, self.y)

    def handle_events(self, event_x, event_y):
        super(TitleStartImg, self).handle_events(event_x, event_y)

        if self.mouse_on_img_on == True:
            if (self.x1 <= event_x <= self.x2 and self.y1 <= event_y <= self.y2) == False:
                self.mouse_on_img_on = False
                self.mouse_on_img_frame = 0
        elif self.mouse_on_img_on == False:
            if self.x1 <= event_x <= self.x2 and self.y1 <= event_y <= self.y2:
                self.mouse_on_img_on = True
                self.mouse_on_img_frame = 0

    def update(self):
        super(TitleStartImg, self).update()
        if self.mouse_on_img_on == True:
            self.mouse_on_img_frame = (self.mouse_on_img_frame + 1) % self.mouse_on_img_max_frame


class TitleExitImg(IMG_class.IMG):
    def __init__(self, x1, y1, x2, y2):
        super(TitleExitImg, self).__init__(x1, y1, x2, y2, 0, Title_exit_main_img_max_frame)
        self.mouse_on_img_frame = 0
        self.mouse_on_img_max_frame = Title_exit_mouse_on_img_max_frame
        self.mouse_on_img_on = False

    def draw(self):
        super(TitleExitImg, self).draw()
        Title_exit_main_img[self.frame].draw(self.x, self.y)

        if self.mouse_on_img_on == True:
            Title_exit_mouse_on_img[self.mouse_on_img_frame].draw(self.x+20, self.y)

    def handle_events(self, event_x, event_y):
        super(TitleExitImg, self).handle_events(event_x, event_y)
        if self.mouse_on_img_on == True:
            if (self.x1 <= event_x <= self.x2 and self.y1 <= event_y <= self.y2) == False:
                self.mouse_on_img_on = False
                self.mouse_on_img_frame = 0
        elif self.mouse_on_img_on == False:
            if self.x1 <= event_x <= self.x2 and self.y1 <= event_y <= self.y2:
                self.mouse_on_img_on = True
                self.mouse_on_img_frame = 0

    def update(self):
        super(TitleExitImg, self).update()
        if self.mouse_on_img_on == True:
            self.mouse_on_img_frame = (self.mouse_on_img_frame + 1) % self.mouse_on_img_max_frame


def enter():
    global Title_BG_img
    global Title_start_main_img, Title_start_mouse_on_img
    global Title_exit_main_img, Title_exit_mouse_on_img
    global Title_start_img
    global Title_exit_img
    global mx, my
    mx = 800/2
    my = 600/2

    # 출력 좌표, 이미지 사이즈 조정
    Title_start_img = TitleStartImg(80, 380, 400, 496)
    Title_exit_img = TitleExitImg(500, 60, 684, 188)

    # 이미지 로드
    Title_BG_img = load_image('resources\\Title\\Background\\Title_BG.png')
    Title_start_main_img = [load_image('resources\\Title\\Single Player\\single%d%d.png'%(i//10, i%10)) for i in range(0, Title_start_main_img_max_frame)]
    Title_start_mouse_on_img = [load_image('resources\\Title\\Single Player\\English\\singleon%d%d.png'%(i//10, i%10)) for i in range(0, Title_start_mouse_on_img_max_frame)]
    Title_exit_main_img = [load_image('resources\\Title\\Exit\\exit%d%d.png'%(i//10, i%10)) for i in range(0, Title_exit_main_img_max_frame)]
    Title_exit_mouse_on_img = [load_image('resources\\Title\\Exit\\English\\exiton%d%d.png'%(i//10, i%10)) for i in range(0, Title_exit_mouse_on_img_max_frame)]

def exit():
    global Title_BG_img
    global Title_start_main_img, Title_start_mouse_on_img
    global Title_exit_main_img, Title_exit_mouse_on_img

    del Title_BG_img
    del Title_start_main_img
    del Title_start_mouse_on_img
    del Title_exit_main_img
    del Title_exit_mouse_on_img



def handle_events():
    global mx, my
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 600 - event.y
            Title_start_img.handle_events(mx, my)
            Title_exit_img.handle_events(mx, my)

        elif event.type == SDL_MOUSEBUTTONDOWN:
            if Title_start_img.mouse_on_img_on == True:
                pass
                # 여기서 게임 시작
            elif Title_exit_img.mouse_on_img_on == True:
                game_framework.quit()


def update():
    Title_start_img.update()
    Title_exit_img.update()



def draw():
    global mx, my
    clear_canvas()

    Title_BG_img.draw(400, 300)
    Title_start_img.draw()
    Title_exit_img.draw()

    update_canvas()
    delay(0.05)




def pause():
    pass


def resume():
    pass






