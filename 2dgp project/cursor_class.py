import IMG_class
from pico2d import*
import game_world

class Cursor:
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
        self.x = game_world.mx
        self.y = game_world.my
        self.frame.update()


    def draw(self):
        self.image.clip_draw((self.width+3) * (int)(self.frame.current_frame)+2, 279, self.width, self.height, self.x-game_world.screen_x  , self.y-game_world.screen_y )





