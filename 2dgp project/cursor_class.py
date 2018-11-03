import IMG_class


class Cursor:
    def __init__(self, x, y, max_frame, frame_update_period ):
        self.x = x
        self.y = y
        # 커서 크기, 프레임값 설정
        self.width = 41
        self.height = 41
        self.frame = IMG_class.Frame(max_frame)

    def update_cursor_point(self, x, y):
        self.x = x
        self.y = y


    def draw(self):
        Cursor_img.clip_draw((self.width+3) * self.frame.current_frame+2, 279, self.width, self.height, self.x  , self.y )
        self.frame.update()

# 마우스 좌표
mx, my = None, None
cursor = Cursor(0, 0, 5, 10)
Cursor_img = None


def update_mouse_point(x, y):
    global mx, my
    mx = x
    my = 600 - y
    cursor.update_cursor_point(mx, my)


