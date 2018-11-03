import IMG_class
from pico2d import*

class Observer():
    image = None
    width = 36
    height = 34
    max_frame = 26
    ACTION_PER_TIME = 0.5

    acceleration = 0.1
    max_velocity = 1
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.to_x = x
        self.to_y = y
        self.velocity = 0.0
        self.frame = IMG_class.Frame(Observer.max_frame,0)

        if Observer.image == None:
            Observer.image = [
                load_image('resources\\Observer\\%d%d.png' % (i // 10, i % 10)) for i in
                range(0, Observer.max_frame)]

    def get_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class Scourge():
    def __init__(self):
        pass

    def get_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class Wraith():
    def __init__(self):
        pass

    def get_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

