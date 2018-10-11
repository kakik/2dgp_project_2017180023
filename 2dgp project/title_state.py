import game_framework
import main_state
import IMG_class
from pico2d import *

name = "TitleState"


BG_img = None
Start_img1 = None
Start_img2 = None
Exit_img1 = None
Exit_img2 = None

Start_img1_max_frame = 34
Start_img2_max_frame = 59
Exit_img1_max_frame = 49
Exit_img2_max_frame = 29

# 이미지 객체
start_img = None
exit_imt = None


# 마우스 좌표
mx = 0
my = 0
iii = None

class StartImg(IMG_class.IMG):
    def __init__(self, x1, y1, x2, y2):
        super(StartImg, self).__init__(x1, y1, x2, y2, 0, Start_img1_max_frame)
        self.img2_frame = 0
        self.img2_max_frame = Start_img2_max_frame
        self.img2_on = False

    def draw(self):
        super(StartImg, self).draw()
        if self.img2_on == True:
            Start_img2[self.img2_frame].draw(self.x, self.y-60)
        Start_img1[self.frame].draw(self.x, self.y)

    def handle_events(self, event_x, event_y):
        super(StartImg, self).handle_events(event_x, event_y)
        if self.img2_on == True:
            if (self.x1 <= event_x <= self.x2 and self.y1 <= event_y <= self.y2) == False:
                self.img2_on = False
                self.img2_frame = 0
        elif self.img2_on == False:
            if self.x1 <= event_x <= self.x2 and self.y1 <= event_y <= self.y2:
                self.img2_on = True
                self.img2_frame = 0

    def update(self):
        super(StartImg, self).update()
        if self.img2_on == True:
            self.img2_frame = (self.img2_frame + 1) % self.img2_max_frame


class ExitImg(IMG_class.IMG):
    def __init__(self, x1, y1, x2, y2):
        super(ExitImg, self).__init__(x1, y1, x2, y2, 0, Exit_img1_max_frame)
        self.img2_frame = 0
        self.img2_max_frame = Exit_img2_max_frame
        self.img2_on = False

    def draw(self):
        super(ExitImg, self).draw()
        Exit_img1[self.frame].draw(self.x, self.y)

        if self.img2_on == True:
            Exit_img2[self.img2_frame].draw(self.x+20, self.y)

    def handle_events(self, event_x, event_y):
        super(ExitImg, self).handle_events(event_x, event_y)
        if self.img2_on == True:
            if (self.x1 <= event_x <= self.x2 and self.y1 <= event_y <= self.y2) == False:
                self.img2_on = False
                self.img2_frame = 0
        elif self.img2_on == False:
            if self.x1 <= event_x <= self.x2 and self.y1 <= event_y <= self.y2:
                self.img2_on = True
                self.img2_frame = 0

    def update(self):
        super(ExitImg, self).update()
        if self.img2_on == True:
            self.img2_frame = (self.img2_frame + 1) % self.img2_max_frame



def enter():
    global BG_img
    global Start_img1, Start_img2
    global Exit_img1, Exit_img2
    global start_img
    global exit_img
    global mx, my
    global iii
    mx = 800/2
    my = 600/2

    # 출력 좌표, 이미지 사이즈 조정
    start_img = StartImg(80, 380, 400, 496)
    exit_img = ExitImg(500, 60, 684, 188)

    # 이미지 로드
    BG_img = load_image('resources\\Title\\Background\\Title_BG.png')
    Start_img1 = [load_image('resources\\Title\\Single Player\\single%d%d.png'%(i//10, i%10)) for i in range(0, Start_img1_max_frame)]
    Start_img2 = [load_image('resources\\Title\\Single Player\\English\\singleon%d%d.png'%(i//10, i%10)) for i in range(0, Start_img2_max_frame)]
    Exit_img1 = [load_image('resources\\Title\\Exit\\exit%d%d.png'%(i//10, i%10)) for i in range(0, Exit_img1_max_frame)]
    Exit_img2 = [load_image('resources\\Title\\Exit\\English\\exiton%d%d.png'%(i//10, i%10)) for i in range(0, Exit_img2_max_frame)]
    iii = load_image('resources\\Wraith\\0.png')

def exit():
    global BG_img
    del (BG_img)



def handle_events():
    global mx, my
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 600 - event.y
            start_img.handle_events(mx, my)
            exit_img.handle_events(mx, my)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)

def update():
    start_img.update()
    exit_img.update()



def draw():
    global iii
    global mx, my
    clear_canvas()
    BG_img.draw(400, 300)
    start_img.draw()
    exit_img.draw()
    update_canvas()
    iii.draw(mx,my)
    delay(0.05)




def pause():
    pass


def resume():
    pass






