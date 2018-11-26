import cursor_class
from pico2d import *
import game_framework
import game_world
import math




class Frame:
    def __init__(self, max_frame, ACTION_PER_TIME):
        self.current_frame = 0
        self.max_frame = max_frame
        self.ACTION_PER_TIME = ACTION_PER_TIME

    def update(self):
        self.current_frame = (self.current_frame + (self.ACTION_PER_TIME*self.max_frame*game_framework.frame_time)) % (self.max_frame-1)

    def direction_update(self, x_velocity, y_velocity):
        vector1_x = x_velocity / (math.sqrt(x_velocity ** 2 + y_velocity ** 2))
        vector1_y = y_velocity / (math.sqrt(x_velocity ** 2 + y_velocity ** 2))

        cosangle =math.acos(vector1_x*0 + vector1_y*1)  # vector (0,1)과 내적
        if vector1_x*1 - vector1_y*0 <= 0.0 :   # vector (0,1)과 외적
            cosangle = -cosangle

        section_angle =  360.0  / (self.max_frame+1)
        cosangle = cosangle/3.14159265358979*180.0
        cosangle = (cosangle+360.0)%360.0

        for i in range (0,self.max_frame+1):
            if (section_angle*i - section_angle*2)<= cosangle <(section_angle*i + section_angle*2):
                self.current_frame = i
                return



