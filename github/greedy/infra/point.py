# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 19:14
# @Author  : Junzhou Liu
# @FileName: point.py
# @Software: PyCharm
class Point:
    # point on the screen, object to save the information

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def add(self, other):
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def scale(self, factor):
        return Point(self._x * factor, self._y * factor)

