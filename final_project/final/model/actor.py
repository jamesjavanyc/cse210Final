# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 19:09
# @Author  : Junzhou Liu
# @FileName: actor.py
# @Software: PyCharm
from final.infra.color import Color
from final.infra.point import Point


class Actor:
    # interface for all charactor in final_project
    def __init__(self):
        """Constructs a new Actor."""
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def move_next(self, max_x, max_y):
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)



    # getters and setters
    def get_color(self):
        return self._color

    def get_position(self):
        return self._position

    def get_text(self):
        return self._text

    def get_velocity(self):
        return self._velocity

    def set_color(self, color):
        self._color = color

    def set_position(self, position):
        self._position = position

    def set_font_size(self, font_size):
        self._font_size = font_size

    def get_font_size(self):
        return self._font_size

    def set_text(self, text):
        self._text = text

    def set_velocity(self, velocity):
        self._velocity = velocity