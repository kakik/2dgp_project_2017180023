import IMG_class
from pico2d import*
import game_world
import game_framework

class Cursor:
    image = None
    width = 41
    height = 41
    max_frame = 5
    ACTION_PER_TIME = 0.8


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = IMG_class.Frame(5,self.ACTION_PER_TIME)
        if self.image == None:
            Cursor.image = load_image('resources\\Cursor\\cursor.png')
        self.cursor_clicked_x = 0
        self.cursor_clicked_y = 0
        self.cursor_clicked_animation = 0
        self.cursor_clicked_animation_size = 1.0

    def get_events(self):
        self.cursor_clicked_x = self.x
        self.cursor_clicked_y = self.y
        self.cursor_clicked_animation = 1
        self.cursor_clicked_animation_size = 1.0

    def update(self):
        self.x = game_world.mx
        self.y = game_world.my
        self.frame.update()

        if self.cursor_clicked_animation != 0:
            if self.cursor_clicked_animation == 1:
                self.cursor_clicked_animation_size = (self.cursor_clicked_animation_size + (self.ACTION_PER_TIME * 5 * game_framework.frame_time))

                if self.cursor_clicked_animation_size >1.4:
                    self.cursor_clicked_animation = 2

            elif self.cursor_clicked_animation == 2:
                self.cursor_clicked_animation_size = (self.cursor_clicked_animation_size - (self.ACTION_PER_TIME * 5 * game_framework.frame_time))

                if self.cursor_clicked_animation_size <= 1.0:
                    self.cursor_clicked_animation = 0

    def draw(self):
        if self.cursor_clicked_animation != 0:
            self.image.clip_draw(46, 232, 41, 41, self.cursor_clicked_x - game_world.screen_coord_x, self.cursor_clicked_y - game_world.screen_coord_y, self.width * self.cursor_clicked_animation_size, self.height * self.cursor_clicked_animation_size)
        self.image.clip_draw((self.width+3) * (int)(self.frame.current_frame) + 2 , 279, self.width, self.height, self.x - game_world.screen_coord_x, self.y - game_world.screen_coord_y)

