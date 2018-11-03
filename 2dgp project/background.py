import random

from pico2d import *



class FixedBackground:

    def __init__(self):
        self.image = load_image('resources\\Title\\Background\\Title_BG.png') #임시
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_center_object(self, player):
       self.set_center_object(player)


    def draw(self):
        pass


    def update(self, frame_time):
        pass

    def handle_event(self, event):
        pass



class InfiniteBackground:


    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.speed = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_center_object(self, boy):
        self.center_object = boy


    def draw(self):
        pass



    def update(self, frame_time):
        pass


    def handle_event(self, event):
        pass