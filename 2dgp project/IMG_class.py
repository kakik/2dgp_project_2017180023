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



class MenuIMG(IMG):
    Title_start_img = None
    Title_exit_img = None

    def __init__(self, x, y, width, height, max_frame, frame_update_period, menu_type):
        super(MenuIMG, self).__init__(x, y, width, height, max_frame, frame_update_period)
        # 메뉴 타입 1 = title_start 2 = title_exit
        self.menu_type = menu_type

        if MenuIMG.Title_start_img == None:
            MenuIMG.Title_start_img = [load_image('resources\\Title\\Start\\single%d%d.png'%(i//10, i%10)) for i in range(0, max_frame)]
        if MenuIMG.Title_exit_img == None:
            MenuIMG.Title_exit_img = [load_image('resources\\Title\\Exit\\English\\exiton%d%d.png'%(i//10, i%10)) for i in range(0, max_frame)]

    def handle_events(self):
        super(MenuIMG, self).handle_events()

    def update(self):
        super(MenuIMG, self).update()

    def draw(self):
        if self.menu_type == 1:
            MenuIMG.Title_start_img[self.frame.current_frame].draw(self.x, self.y)
        elif self.menu_type == 2:
            MenuIMG.Title_exit_img[self.frame.current_frame].draw(self.x, self.y)

        self.update_frame()


class MenuMouseOnIMG(MenuIMG):
    Title_start_mouse_on_img = None
    Title_exit_mouse_on_img = None

    def __init__(self, x, y, width, height, max_frame, frame_update_period, menu_type):
        super(MenuMouseOnIMG, self).__init__(x, y, width, height, max_frame, frame_update_period, menu_type)

        if MenuMouseOnIMG.Title_start_mouse_on_img == None:
            MenuMouseOnIMG.Title_start_mouse_on_img = [load_image('resources\\Title\\Start\\English\\singleon%d%d.png' % (i // 10, i % 10)) for i in range(0, max_frame)]
        if MenuMouseOnIMG.Title_exit_mouse_on_img == None:
            MenuMouseOnIMG.Title_exit_mouse_on_img = [load_image('resources\\Title\\Exit\\English\\exiton%d%d.png'%(i//10, i%10)) for i in range(0, max_frame)]

    def handle_events(self):
        if self.mouse_on == False:
            super(MenuMouseOnIMG, self).handle_events()
            if self.mouse_on == True:
                self.frame.current_frame = 0
        else:
            super(MenuMouseOnIMG, self).handle_events()


    def update(self):
        super(MenuMouseOnIMG, self).update()

    def draw(self):
        if self.mouse_on == True:
            if self.menu_type == 1:
                MenuMouseOnIMG.Title_start_mouse_on_img[self.frame.current_frame].draw(self.x, self.y - 60)
            elif self.menu_type == 2:
                MenuMouseOnIMG.Title_exit_mouse_on_img[self.frame.current_frame].draw(self.x + 20, self.y)

            self.update_frame()


class Frame:
    def __init__(self, max_frame, frame_update_period):
        self.current_frame = 0
        self.max_frame = max_frame
        self.temp_frame_count = 0
        self.frame_update_period = frame_update_period

    def update(self):
        self.temp_frame_count += 1
        if self.temp_frame_count == self.frame_update_period:
            self.current_frame = (self.current_frame + 1) % self.max_frame
            self.temp_frame_count = 0







