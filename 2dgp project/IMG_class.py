
class IMG(object):
    def __init__(self, x1, y1, x2,  y2, frame, max_frame):
        # 이미지 두 점 좌표
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        # 이미지 출력 좌표
        self.x = (self.x1 + self.x2)/2
        self.y = (self.y1 + self.y2) / 2

        self.frame = frame
        self.max_frame = max_frame


    def draw(self):
        pass

    def update(self):
        self.frame = (self.frame+1) % self.max_frame

    def handle_events(self, event_x, event_y):
        pass

