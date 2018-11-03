import title_state
import cursor_class
from pico2d import *

class IMG(object):
    def __init__(self, x, y, width, height, max_frame, frame_update_period): # 두 점의 좌표로 초기화
        # 이미지 두 점 좌표
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # 출력을 위한 프레임
        self.frame = Frame(max_frame, frame_update_period)
        self.mouse_on = False

        # 충돌체크를 위한 두 점 좌표값
        self.x1 = self.x - (self.width/2)
        self.y1 = self.y - (self.height / 2)
        self.x2 = self.x + (self.width / 2)
        self.y2 = self.y + (self.height / 2)


    def draw(self):
        pass

    def update(self):
        pass

    def handle_events(self):
        # 마우스 충돌체크
        if self.mouse_on == False:
            if (self.x1 <= cursor_class.mx <= self.x2) and (self.y1 <= cursor_class.my <= self.y2):
                self.mouse_on = True
        else:
            if ((self.x1 <= cursor_class.mx <= self.x2) and (self.y1 <= cursor_class.my <= self.y2)) == False:
                self.mouse_on = False

    def update_frame(self):
        self.frame.update()

    Title_start_mouse_on_img_max_frame = 60
    Title_exit_img_max_frame = 50
    Title_exit_mouse_on_img_max_frame = 30

    # 객체 생성! 출력 좌표, 이미지 사이즈 조정은 여기서

    Title_start_mouse_on = IMG_class.MenuMouseOnIMG(240, 438, 320, 116, Title_start_mouse_on_img_max_frame, 4, 1)
    Title_exit = IMG_class.MenuIMG(592, 122, 184, 128, Title_exit_img_max_frame, 4, 2)
    Title_exit_mouse_on = IMG_class.MenuMouseOnIMG(592, 122, 184, 128, Title_exit_mouse_on_img_max_frame, 4, 2)


class MenuStartIMG():
    image = None
    width = 320
    height = 116
    max_frame = 35

    def __init__(self):
        self.x = 240
        self.y = 438

        self.frame = Frame(MenuStartIMG.max_frame)
        self.mouse_on = False

        if MenuStartIMG.image == None:
            MenuStartIMG.image = [load_image('resources\\Title\\Start\\single%d%d.png'%(i//10, i%10)) for i in range(0, MenuStartIMG.max_frame)]


    def handle_events(self):
        # 마우스 충돌체크
        if (self.x - MenuStartIMG.width/2 <= cursor_class.mx <= self.x + MenuStartIMG.width/2) and (self.y- MenuStartIMG.height/2 <= cursor_class.my <= self.y + MenuStartIMG.height/2):
            if self.mouse_on == False:
                self.mouse_on = True
        else:
            if self.mouse_on == False:
                self.mouse_on = True

    def update(self):
        self.frame.update()

    def draw(self):
        MenuStartIMG.image[self.frame.current_frame].draw(self.x, self.y)



class MenuExitIMG():
    image = None
    width = 184
    height = 128
    max_frame = 50

    def __init__(self):
        self.x = 592
        self.y = 122

        self.frame = Frame(MenuExitIMG.max_frame)
        self.mouse_on = False

        if MenuExitIMG.image == None:
            MenuStartIMG.image = [load_image('resources\\Title\\Exit\\English\\exiton%d%d.png' % (i // 10, i % 10))  for i in range(0, MenuExitIMG.max_frame)]

    def handle_events(self):
        # 마우스 충돌체크
        if (self.x - MenuExitIMG.width / 2 <= cursor_class.mx <= self.x + MenuExitIMG.width / 2) and (
                self.y - MenuExitIMG.height / 2 <= cursor_class.my <= self.y + MenuExitIMG.height / 2):
            if self.mouse_on == False:
                self.mouse_on = True
        else:
            if self.mouse_on == False:
                self.mouse_on = True

    def update(self):
        self.frame.update()

    def draw(self):
        MenuExitIMG.image[self.frame.current_frame].draw(self.x, self.y)


class MenuStartMouseOnIMG():
    image = None
    width = 320
    height = 116
    max_frame = 60

    def __init__(self):
        self.x = 240
        self.y = 438

        self.frame = Frame(MenuStartMouseOnIMG.max_frame)
        self.mouse_on = False

        if MenuStartMouseOnIMG.image == None:
            MenuStartMouseOnIMG.image =[load_image('resources\\Title\\Start\\English\\singleon%d%d.png' % (i // 10, i % 10)) for i in range(0, MenuStartMouseOnIMG.max_frame)]

    def handle_events(self):
        # 마우스 충돌체크
        if (self.x - MenuStartMouseOnIMG.width / 2 <= cursor_class.mx <= self.x + MenuStartMouseOnIMG.width / 2) and (
                self.y - MenuStartMouseOnIMG.height / 2 <= cursor_class.my <= self.y + MenuStartMouseOnIMG.height / 2):
            if self.mouse_on == False:
                self.mouse_on = True
        else:
            if self.mouse_on == False:
                self.mouse_on = True

    def update(self):
        self.frame.update()

    def draw(self):
        MenuStartMouseOnIMG.image[self.frame.current_frame].draw(self.x, self.y)


class MenuExitMouseOnIMG():
    image = None
    width = 184
    height = 128
    max_frame = 30

    def __init__(self):
        self.x = 592
        self.y = 122

        self.frame = Frame(MenuExitMouseOnIMG.max_frame)
        self.mouse_on = False

        if MenuExitMouseOnIMG.image == None:
            MenuExitMouseOnIMG.image = [load_image('resources\\Title\\Exit\\English\\exiton%d%d.png'%(i//10, i%10)) for i in range(0, MenuExitMouseOnIMG.max_frame)]

    def handle_events(self):
        # 마우스 충돌체크
        if (self.x - MenuExitMouseOnIMG.width / 2 <= cursor_class.mx <= self.x + MenuExitMouseOnIMG.width / 2) and (
                self.y - MenuExitMouseOnIMG.height / 2 <= cursor_class.my <= self.y + MenuExitMouseOnIMG.height / 2):
            if self.mouse_on == False:
                self.mouse_on = True
        else:
            if self.mouse_on == False:
                self.mouse_on = True

    def update(self):
        self.frame.update()

    def draw(self):
        MenuExitMouseOnIMG.image[self.frame.current_frame].draw(self.x, self.y)








class Frame:
    def __init__(self, max_frame):
        self.current_frame = 0
        self.max_frame = max_frame

    def update(self):
        self.current_frame = (self.current_frame + 1) % self.max_frame
