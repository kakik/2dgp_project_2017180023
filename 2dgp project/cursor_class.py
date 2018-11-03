import IMG_class
from pico2d import*


class Cursor:
    global mx, my
    image = None
    width = 41
    height = 41
    max_frame = 5
    ACTION_PER_TIME = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = IMG_class.Frame(5,self.ACTION_PER_TIME)
        if self.image == None:
            Cursor.image = load_image('resources\\Cursor\\cursor.png')

    def handle_events(self):
        pass

    def update(self):
        self.x = mx
        self.y = my
        self.frame.update()


    def draw(self):
        self.image.clip_draw((self.width+3) * (int)(self.frame.current_frame)+2, 279, self.width, self.height, self.x  , self.y )

cursor = None

# 마우스 좌표
mx, my = None, None

def update_mouse_point(x, y):
    global mx, my
    mx = x
    my = 600 - y


